from urllib import request, parse
import json
class Database():
    Data = dict
    def Run(self):
        pass
    def RunSpecial(self):
        pass
    def Get(self):
        content = request.urlopen("https://sit312-mirror.mybluemix.net/api/user/getUsers").read().decode("utf-8")
        self.Data = json.loads(content)
    def Post(self, data):
        data = parse.urlencode(data).encode()
        req = request.Request("https://sit312-mirror.mybluemix.net/api/user/register", data=data)
        resp = request.urlopen(req)
        self.Get()

if __name__ == "__main__":
    a = Database()
    data = {"name":"Jack", "age":"20", "Location":"Australia", "Nurse":"Kapish", "Medication":"Dementia"}
    a.Get()
    print(a.Data)
    a.Post(data)
    print()

