#!/usr/bin/env python3

from urllib.request import urlopen
import json
import configparser

if __name__ != "__main__":
    from components.Standard import Standard

class Weather():
    """Obtain current weather information

    This class uses API from OpenWeatherMap.org to obtain the weather information.
    The information is presented in dict format.
    """

    Data = None #dict
    APIKey = None #string
    CityID = None #string
    CityName = None #string
    CountryCode = None #string
    def __init__(self, api_key = None, city_id = None, city_name = None, country_code = None):
        self.APIKey = api_key
        self.CityID = city_id
        self.CityName = city_name
        self.CountryCode = country_code
        
    def GetWeatherByID(self):
        """Uses city ID to get the current weather"""
        
        if self.APIKey == None or self.CityID == None:
            return None
        else:
            response = urlopen("https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(self.CityID, self.APIKey)).read().decode("utf-8") 
            self.Data = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data
        
    def GetWeatherByCity(self):
        """Uses city name to get the current weather"""
        
        if self.APIKey == None or self.CityName == None:
            return None
        else:
            response = urlopen("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(self.CityName, self.APIKey)).read().decode("utf-8") 
            self.Data = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data
    
    def RunSpecial(self):
        pass
    def _UpdateInformation(self, data):
        """Upates all the variable in the class based on self.Data"""

        if self.Data != None:
            self.CityID = data["id"]
            self.CityName = data["name"]
            self.CountryCode = data["sys"]["country"]
        else:
            return None

    def Run(self):
        """Run function for the mirror"""
        config = configparser.ConfigParser()
        config.read("components/configuration.ini")
        self.APIKey = config["Weather"]["APIKey"]
        self.CityID = "2144728"
        self.CityName = "wantirna south"
        self.GetWeatherByID()
        standard = Standard()
        standard.UpdateTextByTag("weathercurrenttemp", str(self.Data["main"]["temp"])+"°C")
        standard.UpdateTextByTag("weatherlocation", str(self.Data["name"]))
        standard.UpdateTextByTag("weathermintemp", str(self.Data["main"]["temp_min"])+"°C")
        standard.UpdateTextByTag("weathermaxtemp", str(self.Data["main"]["temp_max"])+"°C")
        standard.Commit()

if __name__ == "__main__":
    APIKey = "fe567241f2e7dae1e8bd917c752f84f9"
    cityid = "2144728"
    cityname = "wantirna south"
    a = Weather(api_key= APIKey,city_id= cityid)
    print(a.GetWeatherByID())
