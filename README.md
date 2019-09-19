# Smart Mirror/Mindful Mirror :framed_picture:

![Prdoject Demo](https://media.giphy.com/media/47EtjlHYFREM5Rznaf/giphy.gif)

Project for SIT312 System Design and Prototyping @ Deakin

The Mindful Mirror is a open source project aimed at trying to solve not only the cost associated with treating Alzheimer’s disease which is currently the most common form of dementia affecting up to 70% of all people with dementia. However, it also aims to help alleviate the stress that loved one’s face when caring for family members at home or while they are in aged care homes as people with dementia account for 52% of all residents in residential aged care facilities.

## Getting Started/How To Use :children_crossing:

Enable i2c on RPi
- Run ```sudo raspi-config```
- Select ```Interfacing Options```
- Select ```I2C```
- Select ```Yes```

Install the python3 modules on Prerequisites

Place wiring as shown:

| Board Pin | Function     |  RPi Pin | RPi Function   |
|-----------|--------------|----------|----------------|
| GND       | Ground       |  P01-9   | GND
| VCC       | +3.3V        |  P01-1   | 3.3V PWR
| SDA       | Data         |  P01-3   | I2C1 SDA
| SCL       | Clock        |  P01-5   | I2C1 SCL
| INT       | Interrupt    |  P01-7   | GPIO 4

Clone the git repository and launch client.py

### Prerequisites

- Python 3.x :snake:
- Raspberry Pi (RPi)
- pip3 for RPi
- apds9960 module for RPi python3
- smbus module for RPi python3
- tkinter module for RPi python3
- Active internet connection
- NodeRed set up with a specific cloud Database

## Build your own module :electron:

Adhere to the following rules when trying to build a custom module
- Place module in components/
- Name the python file as the same name as the class inside
- Include a .Run() method inside your class. This will run every 120 seconds when the mirror is active
```
# Example.py
class Example:
    def Run(self):
        # method here
```
- When including other modules in .Run(), make the path as you would coding from root folder
```
#foo.py
class foo:
    def method(self):
        # foo method here

#bar.py
from components.foo import foo #<---
class bar:
    def Run(self):
        foo.method()
```
- When using Standard, make sure to run .Commit() to make changes to clientgui.json 
```
Standard().Commit()
```


## Sending and Receiving Data :file_folder:

In order to send and recieve data you simply just need to set a GET or POST request to the database. The following commands built into the database are the following:

* GET (Returns all users in the database) - https://sit312-mirror.mybluemix.net/api/user/getUsers
* POST (Add's a user to the database) - https://sit312-mirror.mybluemix.net/api/user/register
* GET, specific user (We use the unique user ID to get a specific user) - https://sit312-mirror.mybluemix.net/api/user/getSpecUsers?_id=UserID

## Contributors :bowtie:

* **Jack Murley** - [GitHub](https://github.com/JTMurley)
* **Kai Zhi Lam** - [GitHub](https://github.com/kaizhilam)
* **Tristan Skadins**
* **Kapish Dandona**

## Acknowledgments :basecamp:

* OpenWeatherMap
* NewsAPI
* liske for the [python-apds9960](https://github.com/liske/python-apds9960)

## Trello :calendar:

[Trello](https://trello.com/invite/b/dhC3HB7k/4754cb65c0d6cbff4c509aed8d64d80a/sit312)
