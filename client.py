from tkinter import *
import json
import threading
import time
import sys
import os

class Mirror():
    """UI for the mirror"""

    UIElements = [] #list
    __Threading = True
    __ThreadList = [] #list

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
        self.__ThreadList.append(threading.Thread(target=self.__UpdateGUI, daemon=True))
        self.__ThreadList.append(threading.Thread(target=self.__Update, daemon=True))
        for i in self.__ThreadList:
            i.start()
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

    def __UpdateGUI(self):
        """Check if there are any change in the JSON file and then
            updating all the element from the JSON file"""

        with open("clientgui.json") as file:
            current = file.read()
        new = current
        while self.__Threading:
            print("Updating GUI...")
            with open("clientgui.json") as file:
                new = file.read()
            if current != new:
                current = new
                try:
                    temp = json.loads(new)
                    for i in self.UIElements:
                        i.destroy()
                    self.UIElements.clear()
                    self.__Populate()
                except:
                    print("JSON file error")
            time.sleep(0.5)


    def Shutdown(self, e):
        self.__Threading = False
        self.root.destroy()
    
    def __Update(self):
        while self.__Threading:
            print("Updating widgets...")
            directories = os.listdir("components")
            for i in directories:
                if i[-3:].lower() == ".py":
                    exec("from components.{} import {}".format(i[:-3], i[:-3]))
                    exec("{}().Run()".format(i[:-3]))
            time.sleep(120)    

#Mirror(ScreenWidth, ScreenHeight, BackgroundColour)
if __name__ == "__main__":
    main = Mirror()

