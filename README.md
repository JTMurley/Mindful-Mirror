# Smart Mirror

Project for SIT312 System Design and Prototyping @ Deakin

## Getting Started

Clone the git repository and launch client.py

### Prerequisites

- Python 3.x
- Raspberry Pi

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
