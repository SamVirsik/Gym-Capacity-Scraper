# Gym-Capacity-Scraper
A Python scraper and analysis of the Berkeley gym capacity at UC Berkeley to find the best workout times. 

## Overview
This is a project I undertook to scrape and analyze the capacity of the Berkeley Gym (RSF) over an extended time to find the best times to go to the gym. Through it I have determined the times in which the gym is the least full, and so I go during these times so that I can keep my workouts efficient. 

## File Specifics
### ScrapingFunctionality and AutomatedScraping
These are the two scraping-related files. One includes the basic functionality for scraping and the other runs the process continuously. The entire project is possible because the RSF has a website which tracks the capacity of the gym in real-time. They are, however, unwilling to share historic data publicly, so continuous scraping is needed to observe trends over time. 

### Visualizing
This is a simply jupyter notebook to visualize the results. Since the data is stored with its timestamp, one can very easily see trends for any given day which was tracked. 

## Functionality and Technologies
Scrapes capacity every 30 seconds  
Stores capacity and timestamp in CSV  
Does so using Selenium to wait for Javascript page underlying HTML to update  

Libraries: BeautifulSoup, Requests, Selenium, Pandas
