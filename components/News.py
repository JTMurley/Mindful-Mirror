#!/usr/bin/env python3

from urllib.request import urlopen
import json
import configparser

if __name__ != "__main__":
    from components.Standard import Standard

class News:
    """News library"""

    Data = None #dict
    def __init__(self, api_key = None, country_code = None):
        self.APIKey = api_key
        self.CountryCode = country_code
    def RunSpecial(self):
        pass    
    def GetNews(self):
        """Get news from newsapi.org"""
        if self.APIKey == None or self.CountryCode == None:
            return None
        else:
            response = urlopen("https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(self.CountryCode, self.APIKey)).read().decode("utf-8") 
            self.Data = json.loads(response)
            return self.Data

    def Run(self):
        """Run function for the mirror"""

        config = configparser.ConfigParser()
        config.read("components/configuration.ini")
        self.APIKey = config["News"]["APIKey"]
        self.CountryCode = "au"
        self.GetNews()
        standard = Standard()
        self.GetNews()
        text = ""
        for i in range(0,5):
            text += "- {}\n\n".format(standard.FormatSentence(self.Data["articles"][i]["title"], 35))
        standard.UpdateTextByTag("newstitle", text)
        standard.Commit()

if __name__ == "__main__":
    from Standard import Standard
    APIKey = "c3766bcb72d847699e339f3dd0181c1a"
    main = News(api_key=APIKey,country_code="au")
    main.GetNews()
    print(main.Data)
        
