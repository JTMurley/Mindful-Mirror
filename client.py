from tkinter import *
import json
import threading
import time

class Mirror():
    """UI for the mirror"""
    
    UIElements:list = []

    def __init__(self, screenWidth = None, screenHeight = None, backgroundColour = "black"):
        self.ScreenWidth = screenWidth
        self.ScreenHeight = screenHeight
        self.BackgroundColour = backgroundColour
        self.root = Tk()
        root = self.root
        if self.ScreenWidth == None: self.ScreenWidth = root.winfo_screenwidth()
        if self.ScreenHeight == None: self.ScreenHeight = root.winfo_screenheight()
        root.geometry(str(self.ScreenWidth)+"x"+str(self.ScreenHeight))
        root.resizable(width = FALSE, height = FALSE)
        root.config(bg = self.BackgroundColour, cursor = "None")
        root.bind("<Escape>", self.Shutdown) #binds ESC key to shut down mirror
        root.overrideredirect(True) #remove title bar
        self.__Populate()
        updategui = threading.Thread(target=self.__Update);
        updategui.start()
        root.mainloop()
    
    def __Populate(self):
        """Populating elements inside the Tkinter GUI with clientgui.JSON"""

        with open("clientgui.json") as file:
            data = json.load(file)
        for i in data:
            if i["x"] < 0:
                x = self.root.winfo_screenwidth()+i["x"]
            else:
                x = i["x"]
            if i["y"] < 0:
                y = self.root.winfo_screenheight()+i["y"]
            else:
                y = i["y"]
            if i["type"] == "label":
                item = Label(self.root, 
                text = i["text"],
                font = (i["font"], i["font size"]),
                fg=i["font colour"],
                width = i["width"], 
                height = i["height"],
                bg=self.BackgroundColour)
                item.place(x = x, y = y)
                self.UIElements.append(item)

    def __Update(self):
        """Updating all the element from the JSON file"""

        file = open("clientgui.json")
        current = file.read()
        file.close()    
        while True:
            time.sleep(60)
            file = open("clientgui.json")
            new = file.read()
            file.close()
            if current != new:
                current = new
                for i in self.UIElements:
                    i.destroy()
                self.UIElements.clear()
                print(self.UIElements)
                self.__Populate()

    def Shutdown(self, e):
        exit()

    

#Mirror(ScreenWidth, ScreenHeight, BackgroundColour)
Mirror()


