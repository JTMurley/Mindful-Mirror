from urllib import request, parse
import json
import configparser

if __name__ != "__main__":
    from components.Standard import Standard

class Database():
    Data = dict
    def __init__(self):
        config = configparser.ConfigParser()
        if __name__ == "__main__":
            config.read("configuration.ini")
        else:
            config.read("components/configuration.ini")
        self.__ID = config["Database"]["ID"]
    def Run(self):
        self.Get()
        standard = Standard()
        print(self.Data["name"])
        print(self.Data["age"])
        print(self.Data["Nurse"])
        print(self.Data["Medication"])
        standard.UpdateTextByTag("databasename", "Name: {}".format(self.Data["name"]))
        standard.UpdateTextByTag("databaseage", "Age: {}".format(self.Data["age"]))
        standard.UpdateTextByTag("databasenurse", "Nurse: {}".format(self.Data["Nurse"]))
        standard.UpdateTextByTag("databasemedication", "Medication: {}".format(self.Data["Medication"]))
        standard.Commit()
    def RunSpecial(self):
        pass
    def Get(self):
        content = request.urlopen("https://sit312-mirror.mybluemix.net/api/user/getSpecUsers?_id={}".format(self.__ID)).read().decode("utf-8")
        self.Data = json.loads(content)
    # def Post(self, data):
    #     data = parse.urlencode(data).encode()
    #     req = request.Request("https://sit312-mirror.mybluemix.net/api/user/register", data=data)
    #     resp = request.urlopen(req)
    #     self.Get()

if __name__ == "__main__":
    a = Database()
    data = {"name":"Jack", "age":"20", "Location":"Australia", "Nurse":"Kapish", "Medication":"Dementia"}
    a.Get()
    print(a.Data["name"])
    # a.Post(data)
    # print()

