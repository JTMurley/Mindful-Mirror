#!/usr/bin/env python3

DEBUGFROMWINDOWS = False #Disable GPIO and sensors library
DEBUG = True #Print log

from tkinter import *
import json
import threading
import time
import os

if DEBUGFROMWINDOWS == False:
    from apds9960.const import *
    from apds9960 import APDS9960
    import RPi.GPIO as GPIO
    import smbus

class Mirror():
    """UI for the mirror"""

    UIElements = [] #list
    __Threading = False
    __ThreadList = [] #list
    if DEBUGFROMWINDOWS == True: __ShowGUI = True

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
        root.config(cursor = "none") #Remove cursor
        root.bind("<Escape>", self.Shutdown) #binds ESC key to shut down mirror
        root.wm_attributes("-fullscreen", "true") #remove title bar
        self.__Populate()
        if DEBUGFROMWINDOWS == False:
            port = 1
            bus = smbus.SMBus(port)
            self.apds = APDS9960(bus)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.IN)
            self.dirs = {APDS9960_DIR_NONE: "none",
                    APDS9960_DIR_LEFT: "left",
                    APDS9960_DIR_RIGHT: "right",
                    APDS9960_DIR_UP: "up",
                    APDS9960_DIR_DOWN: "down",
                    APDS9960_DIR_NEAR: "near",
                    APDS9960_DIR_FAR: "far"}
            try:
                # Interrupt-Event hinzufuegen, steigende Flanke
                GPIO.add_event_detect(7, GPIO.FALLING, callback = self.__intH)
                self.apds.setProximityIntLowThreshold(50)
                print("Gesture Test")
                print("============")
                self.apds.enableGestureSensor()
            finally:
                pass
        self.__ThreadList.append(threading.Thread(target=self.__Sense, daemon=True))
        self.__ThreadList.append(threading.Thread(target=self.__Update, daemon=True))
        self.__ThreadList.append(threading.Thread(target=self.__UpdateSpecial, daemon=True))
        for i in self.__ThreadList:
            i.start()
        if DEBUGFROMWINDOWS == True: root.bind("<Return>", self.__DebugTestGUI)
        root.mainloop()
    
    def __Populate(self):
        """Populating elements inside the Tkinter GUI with clientgui.JSON"""

        if DEBUG == True: print("Starting to populate GUI items")
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
                             bg=self.BackgroundColour, 
                             anchor=W, 
                             justify=LEFT)
            elif i["type"] == "button":
                item = Button(self.root,
                              width = i["width"],
                              height = i["height"],
                              bg=self.BackgroundColour)
                              #relief="flat")
            elif i["type"] == "image":
                item = Label(self.root,
                             width = i["width"],
                             height = i["height"],
                             bg=self.BackgroundColour, 
                             anchor=W, 
                             justify=LEFT)
            #contain constructor
            if "text" in i:
                item.config(text = i["text"],
                            font = (i["font"], i["font size"]),
                            fg=i["font colour"])
            elif "image" in i:
                photo = PhotoImage(file = i["image"])
                if "zoom" in i:
                    photo = photo.zoom(i["zoom"])
                if "subsample" in i:
                    photo = photo.subsample(i["subsample"])
                item.config(image = photo)
                item.image = photo
            item.place(x = x, y = y)
            self.UIElements.append(item)
        if DEBUG == True: print("Finish populating GUI items")

    def Shutdown(self, e):
        if DEBUGFROMWINDOWS == False:
            GPIO.cleanup()
        self.__Threading = False
        self.root.destroy()

    
    def __Update(self):
        """ Update GUI and Runs .Run() function from each library in /component"""

        with open("clientgui.json") as file:
            current = file.read()
        new = current
        while self.__Threading:
            if DEBUG == True: print("Start .Run()")
            #.Run() for every library
            directories = os.listdir("components")
            for i in directories:
                if i[-3:].lower() == ".py":
                    exec("from components.{} import {}".format(i[:-3], i[:-3]))
                    exec("{}().Run()".format(i[:-3]))
            #update GUI
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
                    if DEBUG == True: 
                        print("JSON file error")
                    else: 
                        self.Shutdown(1)
            time.sleep(120)  
    
    def __UpdateSpecial(self):
        """ Update GUI and Runs .Run() function from each library in /component"""

        with open("clientgui.json") as file:
            current = file.read()
        new = current
        while self.__Threading:
            if DEBUG == True: print("Start .RunSpecial()")
            #.Run() for every library
            directories = os.listdir("components")
            for i in directories:
                if i[-3:].lower() == ".py":
                    exec("from components.{} import {}".format(i[:-3], i[:-3]))
                    try:
                        exec("{}().RunSpecial()".format(i[:-3]))
                    except:
                        print("No RunSpecial for module {}".format(i[:-3]))
            #update GUI
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
                    if DEBUG == True: 
                        print("JSON file error")
                    else: 
                        self.Shutdown(1)
            time.sleep(10)  

    def __Sense(self):
        while self.__Threading and DEBUGFROMWINDOWS==False:
            time.sleep(0.5)
            if self.apds.isGestureAvailable():
                motion = self.apds.readGesture()
                if DEBUG == True: print("Gesture={}".format(self.dirs.get(motion, "unknown")))
                if self.dirs.get(motion) == "up" or self.dirs.get(motion) == "left":
                    for i in self.UIElements:
                        i.destroy()
                    self.UIElements.clear()
                elif self.dirs.get(motion) == "down" or self.dirs.get(motion) == "right":
                    self.__Populate()
    
    def __DebugTestGUI(self, event):
        if self.__ShowGUI == True:
            for i in self.UIElements:
                i.destroy()
            self.__ShowGUI = False
        else:
            self.__Populate()
            self.__ShowGUI = True
    
    def __intH(self, channel):
        if DEBUG == True: print("INTERRUPT")




#Mirror(ScreenWidth, ScreenHeight, BackgroundColour)
if __name__ == "__main__":
    main = Mirror()

