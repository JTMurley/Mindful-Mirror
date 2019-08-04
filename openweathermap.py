from urllib.request import urlopen
import json

class Weather():
    """Obtain current weather information

    This class uses API from OpenWeatherMap.org to obtain the weather information.
    The information is presented in dict format.
    """
    
    Data:dict = None
    APIKey:str = None
    CityID:str = None
    CityName:str = None
    CountryCode:str = None
    def __init__(self, api_key:str = None, city_id:str = None, city_name:str = None, country_code:str = None):
        self.APIKey = api_key
        self.CityID = city_id
        self.CityName = city_name
        self.CountryCode = country_code
        
    def GetWeatherByID(self):
        """Uses city ID to get the current weather"""
        
        if self.APIKey == None or self.CityID == None:
            return None
        else:
            response = urlopen("https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(self.CityID, self.APIKey)).read()
            self.Data = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data
        
    def GetWeatherByCity(self):
        """Uses city name to get the current weather"""
        
        if self.APIKey == None or self.CityName == None:
            return None
        else:
            response = urlopen("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(self.CityName, self.APIKey)).read()
            self.Data = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data
        
    def _UpdateInformation(self, data):
        """Upates all the variable in the class based on self.Data"""

        if self.Data != None:
            self.CityID = data["id"]
            self.CityName = data["name"]
            self.CountryCode = data["sys"]["country"]
        else:
            return None

#Test
'''
APIKey = "fe567241f2e7dae1e8bd917c752f84f9"
cityid = "2144728"
cityname = "wantirna south"
a = Weather(api_key=APIKey, city_id= cityid)
'''
