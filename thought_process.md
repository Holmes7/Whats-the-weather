# What's The Weather

### Project Synopsis
The project takes a city or latitude and longitude as input and gives the user
1. Weather Description
2. Maximum and Minimum temperature
3. Humidity
4. Timezone

Weather data is scraped from [Weather]( https://weather.com/en-IN/) and Timezone is scraped from [Time and Date](https://www.timeanddate.com). The csv file data used for the project is [here](https://simplemaps.com/data/world-cities).
### Approach and Problems encountered
To get started with web scraping I watched Corey Schafer's video on the topic.
I used Python 3.7 for the project. I used the [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
library as it is the most popular python library for pulling data out of websites. The lxml parser is also used for the project as it is recommended in the BeautifulSoup4 documentation. The usual requests library is used to get the html file from the browser which is loaded into beautifulsoup. The csv module is used to extract data from the csv file.
#### Object Oriented approach
This is my first project where I tried to take the OOP approach. So I had to read a couple of articles to learn it.
#### The link to the weather page of the desired city
I kept a string of link to the basic weather.com page and when we get the input of lat and long the link is appended accordingly so that the desired page is stored in the final link.
#### Description of weather and Humidity
The weather.com page had the description and the weather on the 'today' page after the search itself so it was easy to get it.
#### Maximim and Minimum Temperature
The maximum and minimum temperature section on the first page was getting interchanged so I went to the page with 'hourbyhour' temperature of the city and looped through the values to get maximum and minimum temperature.
#### Timezone
This took the most time for me as it wasn't on the weather.com page and the other page I looked at didn't have a specific page dedicated to it. So pulling information out became a trouble. Then I found the timeanddate website but the link here wanted country and city name as argument. Up until now I just used the latitude and longitude as argument.
#### Getting City name from Lat/Lon and vice versa
The main page after a simple search on google gives the Latitude and Longitude to desired city. But I wasn't able to extract data from this page. With less time on my hands I switched over to get a list of latitudes and longitudes with city names and store it in the project itself. I used to csv module to read the data.
#### Floating point lat/lon
This created a lot of problems for me. It took me a couple of hours to find the simple solution to my problems. I used the math library's isclose() method and problem was solved.

### Still Existing Problems
The csv file isn't complete. So many cities are not found. I will try to solves this by not using csv files at all and trying to get the data directly from a website. Also code is still not commented and documented.
 ### My Experience
 I got to learn a lot during this project. This was my first project trying OOP and I think I have improved quite a bit in that section. I also got to learn HTML a little bit. I also learned about important files in a project like .gitignore, requirements.txt and README.md. With the deadline on my head I tried to complete the project as fast as I could. Making this file was very helpful in understanding the basics of .md files. 