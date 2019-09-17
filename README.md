# Smart Mirror/Mindful Mirror

Project for SIT312 System Design and Prototyping @ Deakin

## Getting Started

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

- Python 3.x
- Raspberry Pi
- pip3 for Rpi
- apds9960 module for RPi python3
- smbus module for RPi python3
- Active internet connection
- NodeRed set up with a specific cloud Database

## Build your own module

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

## Contributors

* **Jack Murley** - [GitHub](https://github.com/JTMurley)
* **Kai Zhi Lam** - [GitHub](https://github.com/kaizhilam)
* **Tristan Skadins**
* **Kapish Dandona**

## Acknowledgments

* OpenWeatherMap
* NewsAPI
* liske for the [python-apds9960](https://github.com/liske/python-apds9960)
