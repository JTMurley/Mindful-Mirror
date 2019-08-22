from urllib.request import urlopen
import json

if __name__ != "__main__":
    from components.Standard import Standard

class News:
    """News library"""
    Data = None #dict
    def __init__(self, api_key = None, country_code = None):
        self.APIKey = api_key
        self.CountryCode = country_code
    
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
        self.APIKey = "c3766bcb72d847699e339f3dd0181c1a"
        self.CountryCode = "au"
        self.GetNews()
        standard = Standard()
        # standard.UpdateTextByTag("currentweather", self.Data["articles"][0]["title"])
        # standard.Commit()

if __name__ == "__main__":
    from Standard import Standard
    APIKey = "c3766bcb72d847699e339f3dd0181c1a"
    main = News(api_key=APIKey, country_code="au")
    main.GetNews()
    print(main.Data["articles"][0]["title"])
