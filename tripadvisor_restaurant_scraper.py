#import libraries
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
import time
import re

#define path for the file
path_to_file = "C:/Users/melis/Desktop/reviews.csv"

#URL to be scrapped
url = "https://www.tripadvisor.fr/Restaurants-g187147-Paris_Ile_de_France.html"

#if inputs passed in command line
if (len(sys.argv) == 3):
    url = sys.argv[1]
    path_to_file = sys.argv[2]
    
#get url
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

#define xpath for "Accept cookie" button and the filter button ("Brunch" in original script)
xpath_cookie_button = "/html/body/div[10]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button"
xpath_filter_button = "/html/body/div[4]/div[3]/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div/label/div/span/span"

#wait for the "Accept cookie" button to be clickable and click on it
btn_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_cookie_button)))
btn_cookies.click()

#wait for the "Brunch" button to be clickable and click on it
btn_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_filter_button)))
btn_filter.click()

#add some time sleep to allow page loading (may be increased in case of low connexion)
time.sleep(3)

#define the items lists
names = []
ratings = []
types = []
urls = []

#scrape content
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
job_elements = soup.findAll("div", class_ = "cauvp Gi o")

for job_element in job_elements:
    #find name and report it as text without the numbering
    name = job_element.find("a", class_ ="bHGqj Cj b").text
    name = re.sub(r'\d', '', name).replace('. ','')
    #find url and report it as complete url
    url = job_element.find("a", class_ ="bHGqj Cj b")['href']
    url = "https://www.tripadvisor.fr" + url
    #find rating and only report the note (remove the "/5 stars" part)
    rating = job_element.find("svg", class_="RWYkj d H0")["aria-label"][:3]
    #find the type of restaurant and report as text
    type = job_element.find("div", class_="bhDlF bPJHV eQXRG")
    type = type.find("span", class_ = "ceUbJ").text
    #append to items lists
    names.append(name)
    ratings.append(rating)
    types.append(type)
    urls.append(url)
    

#turn into dataframe with corresponding columns - you can change values in columns = [] with english words if needed (you will also need to change column name on line 81 then)
df = pd.DataFrame(list(zip(names, types, ratings, urls)), columns = ['Nom', 'Type', 'Note', 'Lien'])

#prepare "url" to be a clickable link in the csv file
df["Lien"] = df["Lien"].apply(lambda x: "=LIEN_HYPERTEXTE(\"" + x + "\")") 

#saving the dataframe as csv with ";" as separator and encoding in latin1
df.to_csv(path_to_file, sep=';', index = False, encoding = "latin1")

#print final message
print("All done, reviews saved at " + path_to_file)


