#!/usr/bin/env python3

from urllib.request import urlopen
import json
import configparser
import datetime

if __name__ != "__main__":
    from components.Standard import Standard

class Weather():
    """Obtain current weather information

    This class uses API from OpenWeatherMap.org to obtain the weather information.
    The information is presented in dict format.
    """

    Data = {"weather":None, "forecast":None} #dict
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
            self.Data["weather"] = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data
        
    def GetWeatherByCity(self):
        """Uses city name to get the current weather"""
        
        if self.APIKey == None or self.CityName == None:
            return None
        else:
            response = urlopen("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(self.CityName, self.APIKey)).read().decode("utf-8") 
            self.Data["weather"] = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data
    
    def RunSpecial(self):
        pass

    def _UpdateInformation(self, data):
        """Upates all the variable in the class based on self.Data"""

        if self.Data["weather"] != None:
            self.CityID = data["weather"]["id"]
            self.CityName = data["weather"]["name"]
            self.CountryCode = data["weather"]["sys"]["country"]
        elif self.Data["forecast"] != None:
            self.CityID = data["forecast"]["city"]["id"]
            self.CityName = data["forecast"]["city"]["name"]
            self.CountryCode = data["forecast"]["city"]["country"]        
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
        standard.UpdateTextByTag("weathercurrenttemp", str(self.Data["weather"]["main"]["temp"])+"°C")
        standard.UpdateTextByTag("weatherlocation", str(self.Data["weather"]["name"]))
        #standard.UpdateTextByTag("weathermintemp", str(self.Data["weather"]["main"]["temp_min"])+"°C")
        #standard.UpdateTextByTag("weathermaxtemp", str(self.Data["weather"]["main"]["temp_max"])+"°C")
        try:
            if self.Data["weather"]["weather"][0]["main"] == "Clear" and datetime.datetime.now().hour >= 8 and datetime.datetime.now().hour <= 20:
                standard.UpdateImageByTag("weathericon", "components/weathericons/{}.gif".format(self.Data["weather"]["weather"][0]["main"]))
            else:
                standard.UpdateImageByTag("weathericon", "components/weathericons/Moon.gif".format(self.Data["weather"]["weather"][0]["main"]))
        except:
            standard.UpdateImageByTag("weathericon", "components/weathericons/Blank.gif")
        #Forecast
        self.GetForecastByID()
        today = datetime.datetime.now().strftime("%a")
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        minimum = float("inf")
        maximum = -float("inf")
        counticon = 0
        result = []
        for i in self.Data["forecast"]["list"]:
            forecasttime = datetime.datetime.fromtimestamp(i["dt"]).strftime("%a")
            if today == forecasttime:
                if i["main"]["temp_min"] < minimum:
                    minimum = int(i["main"]["temp_min"])
                if i["main"]["temp_max"] > maximum:
                    maximum = int(i["main"]["temp_max"])
            else:
                if minimum == float("inf"):
                    pass
                else:
                    result.append([minimum, maximum])
                    minimum = float("inf")
                    maximum = -float("inf")
                    if i["main"]["temp_min"] < minimum:
                        minimum = int(i["main"]["temp_min"])
                    if i["main"]["temp_max"] > maximum:
                        maximum = int(i["main"]["temp_max"])
                today = forecasttime
                counticon += 1
            try:
                standard.UpdateImageByTag("weatherforecasticon{}".format(counticon), "components/weathericons/{}.gif".format(i["weather"][0]["main"]))
            except:
                standard.UpdateImageByTag("weatherforecasticon{}".format(counticon), "components/weathericons/Blank.gif")
        text = ""
        for i in result:
            text += "{}°C - {}°C\n".format(i[0], i[1])
        standard.UpdateTextByTag("weatherforecasttemperature", text)

        text = ""
        for i in range(1,5):
            text += (datetime.date.today() + datetime.timedelta(days=i)).strftime("%a")+" -\n"
        standard.UpdateTextByTag("weatherforecastdays", text)
        
        standard.Commit()
    
    def GetForecastByID(self):
        """Uses city ID to get the forecast"""
        
        if self.APIKey == None or self.CityID == None:
            return None
        else:
            # response = urlopen("https://samples.openweathermap.org/data/2.5/forecast?q=M%C3%BCnchen,DE&appid=b6907d289e10d714a6e88b30761fae22").read().decode("utf-8")
            response = urlopen("https://api.openweathermap.org/data/2.5/forecast?id={}&units=metric&appid={}".format(self.CityID, self.APIKey)).read().decode("utf-8") 
            self.Data["forecast"] = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data

    def GetForecastByCity(self):
        """Uses city ID to get the forecast"""
        
        if self.APIKey == None or self.CityName == None:
            return None
        else:
            response = urlopen("https://api.openweathermap.org/data/2.5/forecast?id={}&units=metric&appid={}".format(self.CityName, self.APIKey)).read().decode("utf-8") 
            self.Data["forecast"] = json.loads(response)
            self._UpdateInformation(self.Data)
            return self.Data
    
if __name__ == "__main__":
    APIKey = "fe567241f2e7dae1e8bd917c752f84f9"
    cityid = "2144728"
    cityname = "wantirna south"
    a = Weather(api_key= APIKey,city_id= cityid)
    a.GetForecastByID()
    a.GetWeatherByID()
    print(a.Data)
