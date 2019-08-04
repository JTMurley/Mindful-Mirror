from tkinter import *

class Mirror():
    def __init__(self, screenWidth = None, screenHeight = None, backgroundColour = "black"):
        self.ScreenWidth = screenWidth
        self.ScreenHeight = screenHeight
        self.BackgroundColour = backgroundColour
        root = Tk()
        if self.ScreenWidth == None: self.ScreenWidth = root.winfo_screenwidth()
        if self.ScreenHeight == None: self.ScreenHeight = root.winfo_screenheight()
        root.geometry(str(self.ScreenWidth)+"x"+str(self.ScreenHeight))
        root.resizable(width = FALSE, height = FALSE)
        root.config(bg = self.BackgroundColour, cursor = "None")
        root.bind("<Escape>", self.Shutdown) #binds ESC key to shut down mirror
        root.overrideredirect(True) #remove title bar
        root.mainloop()

    def Shutdown(self, e):
        exit()

    

#Mirror(ScreenWidth, ScreenHeight, BackgroundColour)
Mirror()


