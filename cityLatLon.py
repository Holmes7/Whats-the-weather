'''import bs4 as BeautifulSoup
import requests


class CityLatLon():
    def getLatLon(self, city):
        self.page_start = 'https://www.google.com/search?&rls=en&q='
        self.page_end = '+latitude+and+longitude&ie=UTF-8&oe=UTF-8'
        self.website_link = self.page_start + city + self.page_end
        self.website_source = requests.get(self.website_link).text
        print(self.website_source)
        self.website_soup = BeautifulSoup(self.website_source, 'lxml')
        self.latlon = self.website_soup.find('div', class_='Z0LcW').text
        self.latitude = ''
        self.longitude = ''
        print(self.latlon)


    #def getCity(self, lat, lon):
        

    #def getCountry(self, lat, lon):
        
'''
import csv
import math

csv_file = open('worldcities.csv', 'r')
csv_reader = csv.reader(csv_file)


class CityLatLon():
    def getLatLon(self, city):
        city = city.lower()
        self.latlon = {}
        for line in csv_reader:
            if line[0].lower() == city:
                self.latlon["latitude"] = line[2]
                self.latlon["longitude"] = line[3]
                break

        return self.latlon

    def getCity(self, lat, lon):
        for line in csv_reader:
            if math.isclose(float(line[2]), float(lat), abs_tol=0.8) and math.isclose(float(line[3]), float(lon), abs_tol=0.8):
                self.city = line[0]
                break

        return self.city

    def getCountry(self, lat, lon):
        for line in csv_reader:
            if math.isclose(float(line[2]), float(lat), abs_tol=0.8) and math.isclose(float(line[3]), float(lon), abs_tol=0.8):
                self.country = line[4]
                break

        return self.country
