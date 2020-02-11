from bs4 import BeautifulSoup
import requests
import cityLatLon


class ScrapeWeather():
    def __init__(self):
        self.website_link = "https://weather.com/en-IN/weather/"
        self.today_link = self.website_link + "today/l/"
        self.hourly_link = self.website_link + "hourbyhour/l/"
        self.timezone_link = "https://www.timeanddate.com/worldclock/"
        self.cityLatLon_obj = cityLatLon.CityLatLon()
        print("Enter 1 for city, 2 for latitude and longitude as input")
        self.type = input()
        if self.type == "2":
            print("Enter Latitude")
            self.latitude = input()
            print("Enter Longitude")
            self.longitude = input()
            self.longitude = str(round(float(self.longitude), 2))
            self.latitude = str(round(float(self.latitude), 2))
            self.city = self.cityLatLon_obj.getCity(self.latitude, self.longitude)
            self.country = self.cityLatLon_obj.getCountry(self.latitude, self.longitude)


        elif self.type == "1":
            print("Enter city")
            self.city = input()
            self.city = self.city.lower()
            self.latlon_dict = self.cityLatLon_obj.getLatLon(self.city)
            self.longitude = str(round(float(self.latlon_dict["longitude"]), 2))
            self.latitude = str(round(float(self.latlon_dict["latitude"]), 2))
            self.country = self.cityLatLon_obj.getCountry(self.latitude, self.longitude)

        self.position = self.latitude + "," + self.longitude
        self.today_link = self.today_link + self.position
        self.hourly_link = self.hourly_link + self.position
        self.timezone_link = self.timezone_link + self.country + '/' + self.city.lower()
        self.today_source = requests.get(self.today_link).text
        self.hourly_source = requests.get(self.hourly_link).text
        self.timezone_source = requests.get(self.timezone_link).text
        self.today_soup = BeautifulSoup(self.today_source, 'lxml')
        self.hourly_soup = BeautifulSoup(self.hourly_source, 'lxml')
        self.timezone_soup = BeautifulSoup(self.timezone_source, 'lxml')

    def getDescription(self):
        self.description = self.today_soup.find('span', class_='today-wx-descrip').text
        print("Description: " + self.description)

    def getMaxMin(self):
        self.table_soup = self.hourly_soup.find('table', class_='twc-table')
        self.temp_soup = self.table_soup.find_all('td', class_='temp')
        self.temp_list = []
        for ind in self.temp_soup:
            temperature = ind.find('span', class_='').text
            self.temp_list.append(temperature)

        self.max_temp = max(self.temp_list)
        self.min_temp = min(self.temp_list)
        print("Maximum Temperature: " + self.max_temp + ' C')
        print("Minimum Temperature: " + self.min_temp + ' C')

    def getHumidity(self):
        self.right_now_soup = self.today_soup.find('div', class_='today_nowcard-sidecar component panel')
        self.row_list = self.right_now_soup.find_all('tr')
        for ind in self.row_list:
            self.row_header = ind.find('th')
            if self.row_header.text == 'Humidity':
                self.humidity = ind.find('span').text
                break

        print("Humidity: " + self.humidity)

    def getTimeZone(self):
        self.timezone_soup = self.timezone_soup.find('div', class_='tile mtt')
        self.timezone_soup = self.timezone_soup.find('div', class_='tl-dt')
        self.timezone = self.timezone_soup.find('small').text
        print(self.timezone)




