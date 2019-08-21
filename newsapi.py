from urllib.request import urlopen
import json

class News:
    Data = None #dict
    def __init__(self, api_key = None, country_code = None):
        self.APIKey = api_key
        self.CountryCode = country_code
    
    def GetNews(self):
        if self.APIKey == None or self.CountryCode == None:
            return None
        else:
            response = urlopen("https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(self.CountryCode, self.APIKey)).read().decode("utf-8") 
            self.Data = json.loads(response)
            return self.Data

if __name__ == "__main__":
    APIKey = "c3766bcb72d847699e339f3dd0181c1a"
    a = News(api_key=APIKey, country_code="au")
    a.GetNews()
    print(a.Data["articles"][0])
