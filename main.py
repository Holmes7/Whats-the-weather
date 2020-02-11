import scrape_weather
import cityLatLon


def main():
    scrape_obj = scrape_weather.ScrapeWeather()
    scrape_obj.getDescription()
    scrape_obj.getMaxMin()
    scrape_obj.getHumidity()
    scrape_obj.getTimeZone()


if __name__ == "__main__":
    main()
