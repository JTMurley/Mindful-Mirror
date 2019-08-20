from tkinter import *
import json
import threading
import time
import sys

class Mirror():
    """UI for the mirror"""

    UIElements = [] #list
    __Threading = True

    def __init__(self, screenWidth = None, screenHeight = None, backgroundColour = "black"):
        self.ScreenWidth = screenWidth #int
        self.ScreenHeight = screenHeight #int
        self.BackgroundColour = backgroundColour #string
        self.root = Tk()
        root = self.root
        if self.ScreenWidth == None: self.ScreenWidth = root.winfo_screenwidth()
        if self.ScreenHeight == None: self.ScreenHeight = root.winfo_screenheight()
        root.geometry(str(self.ScreenWidth)+"x"+str(self.ScreenHeight))
        root.resizable(width = FALSE, height = FALSE)
        root.config(bg = self.BackgroundColour) #Set background
        #root.config(cursor = "None") #Remove cursor
        root.bind("<Escape>", self.Shutdown) #binds ESC key to shut down mirror
        root.overrideredirect(True) #remove title bar
        self.__Populate()
        updategui = threading.Thread(target=self.__Update, daemon=True);
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
            #type constructor
            if i["type"] == "label":
                item = Label(self.root,
                             width = i["width"],
                             height = i["height"],
                             bg=self.BackgroundColour)
            elif i["type"] == "button":
                item = Button(self.root,
                              width = i["width"],
                              height = i["height"],
                              bg=self.BackgroundColour)
                              #relief="flat")
            
            #contain constructor
            if "text" in i:
                item.config(text = i["text"],
                            font = (i["font"], i["font size"]),
                            fg=i["font colour"])
            elif "image" in i:
                photo = PhotoImage(file = i["image"])
                item.config(image = photo)
                item.image = photo
            item.place(x = x, y = y)
            self.UIElements.append(item)

    def __Update(self):
        """Updating all the element from the JSON file"""

        current = self.GUIData()   
        while self.__Threading:
            new = self.GUIData()
            if current != new:
                current = new
                for i in self.UIElements:
                    i.destroy()
                self.UIElements.clear()
                self.__Populate()

    def Shutdown(self, e):
        self.__Threading = False
        self.root.destroy()

    def GUIData(self):
        with open("clientgui.json") as file:
            data = json.load(file)
        return data
    

#Mirror(ScreenWidth, ScreenHeight, BackgroundColour)
if __name__ == "__main__":
    main = Mirror()

