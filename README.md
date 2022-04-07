# Scraping-TripAdvisor-restaurants-with-Python
Scrap TripAdvisor and get restaurants list in CSV with Python 

## Overview
This script scraps in restaurants list from TripAdvisor and extracts some features (name, rating, type, url to restaurant page) in a .csv file. **This script is an exercice for a beginner and still need to be improved (see "Improvements needed" section). At this time, script without any modification will only get brunch restaurants. This will be improved in the next versions.** Also, the final output is in French. 

Just a few features:
- clicks on "Accept cookies" button
- clicks restaurant filter needed, for exemple "Brunch" in the original script (can be modified)

## How to use
Two options :
- download the file, open it and modify variables : url (url to be scrapped), path_to_file (path to final CSV file) and xpath_filter_button (to get another kind of restaurant, it is set to select "brunch" restaurant in the original file). To get the xpath of a button : go to the url, right click on the choosen filter (for exemple "Diner"), click "Inspect". On the right panel, right-click on the line highlighted in blue and choose Copy > Copy full xpath. This feature will be improved in the future. Then just save and run the file.
- launch the file directly from the terminal using the following line : python3 path_to_script url_to_scrap path_to_file (for exemple : python3 ./tripadvisor.py https://www.tripadvisor.fr/Restaurants-g187253-Marseille_Bouches_du_Rhone_Provence_Alpes_Cote_d_Azur.html C:/Users/melis/Desktop/reviews.csv). You can not change filter with this method so you will only have "brunch" restaurants (this will be improved).

Please note that as url input, you need to use restaurants page of a city. Tourism page won't work.

## Improvements needed

### Enable first page scraping
At this time, user has to filter restaurants selection (by price, type of food, or something else) for script to work. On the first page of the URL (i.e. without filtering), for unknown reason at this time, some restaurants get "None" as name when scraping. Need to find out why and fix that.

### Make filter selection easier
At this time, to change filter ("brunch" in the original script), user has to open the file, get xpath of the filter needed and paste it. I think this may be changed by using something else than By.XPATH. It will also be cool if user could select one (or more ?) filter and simply input it in command line.

### Warn the user if a filter is not available for the city choosen
At this time, if user tries to scrap "brunch" restaurants on a city without any brunch restaurant, the script will scrap the next category ("Lunch", for exemple). This is due to TripAdvisor architecture. Fixing the selection filter problem and printing some error message in this case could be nice.

### Get more than one page
At this time, only the page 1 is scraped (30 restaurants). I have to make the script scrap more pages. Maybe the number of pages to scrap could by defined by the user ?

### Debug if user enter "Tourism" url.
It is common that user, by mistake, enter the "Tourism" url instead of "Restaurant" url. If so, it would be nice if the script could navigate to "Restaurants" alone instead of returning empty lists.

## Disclaimer
This script is only a simple exercise for educational purposes. The author cannot be held responsible for any improper use of this script. For any other use of TripAdvisor data user need to request access to the TripAdvisor API and respect the terms and conditions.

## Programming language
Python

## Libraries
Selenium, BeautifulSoup, requests, pandas
