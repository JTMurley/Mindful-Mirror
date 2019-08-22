import json
class Standard:
    def __init__(self):
        if __name__ == "__main__":
            with open("../clientgui.json") as file:
                self.Data = json.load(file)
        else:
            with open("clientgui.json") as file:
                self.Data = json.load(file)

    def UpdateTextByTag(self, tag, text):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["text"] = text

    def UpdateFontByTag(self, tag, font):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["font"] = text

    def UpdateFontSizeByTag(self, tag, font_size):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["font size"] = text

    def UpdateFontColourByTag(self, tag, font_colour):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["font colour"] = text
                self.__UpdateJSON()

    def UpdateXPositionByTag(self, tag, x_position):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["x"] = text

    def UpdateYPositionByTag(self, tag, y_position):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["y"] = text

    def UpdateWidthByTag(self, tag, width):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["width"] = text

    def UpdateHeightByTag(self, tag, height):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["height"] = text

    def Commit(self):
        if __name__ == "__main__":
            with open("../clientgui.json","w") as file:
                json.dump(self.Data, file)
        else:
            with open("clientgui.json","w") as file:
                json.dump(self.Data, file)

    def AddLabelWithText(self, tag = None, text = None, font = "Helvetica", font_size = 8, font_colour = "white", x = 0, y = 0, width = 0, height = 0):
        data = {"tag":tag,
                "type":"label",
                "text":text,
                "font":font,
                "font size":font_size,
                "font colour":font_colour,
                "x":x,
                "y":y,
                "width":width,
                "height":height}
        self.Data.append(data)
    
    def AddLabelWithImage(self, tag = None, image_path = None, x = 0, y = 0, width = 0, height = 0):
        data = {"tag":tag,
                "type":"label",
                "image":image_path,
                "x":x,
                "y":y,
                "width":width,
                "height":height}
        self.Data.append(data)
    
    def RemoveWithTag(self, tag):
        index = None
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                index = n
        if index != None:
            del self.Data[index]

    def Run(self):
        pass
    
    def TagExist(self, tag):
        for i in self.Data:
            if i["tag"] == tag:
                return True
        return False


if __name__ == "__main__":
    main = Standard()
    main.AddLabelWithText(tag="testing")
    print(main.Data)
    main.RemoveWithTag(tag = "testing")
    print(main.Data)
        
