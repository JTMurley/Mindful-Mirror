#!/usr/bin/env python3

import json
class Standard:
    def __init__(self):
        if __name__ == "__main__":
            with open("../clientgui.json") as file:
                self.Data = json.load(file)
        else:
            with open("clientgui.json") as file:
                self.Data = json.load(file)
    
    def RunSpecial(self):
        pass
    
    def Run(self):
        pass

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
    
    def UpdateImageByTag(self, tag, image_location):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                self.Data[n]["image"] = image_location

    def Commit(self):
        if __name__ == "__main__":
            with open("../clientgui.json","w") as file:
                json.dump(self.Data, file)
        else:
            with open("clientgui.json","w") as file:
                json.dump(self.Data, file)
    
    def GetTextByTag(self, tag):
        for n, i in enumerate(self.Data):
            if i["tag"] == tag:
                if "text" in i:
                    return i["text"]
                else:
                    return None

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
    
    def FormatSentence(self, sentence, max_letter):
        """Format sentence by automatically adding \"-\" or a whitespace"""
        
        final = []
        placeholder = ""
        text = sentence.split(" ")
        for words in text:
            if len(words) > max_letter:
                full = []
                temp = ""
                for letters in words:
                    if len(temp) + len(letters) + 1 < 10:
                        temp += letters
                    else:
                        temp += "-"
                        full.append(temp)
                        temp = letters
                full.append(temp)
                final.append("\n".join(full))
            elif len(words) + len(placeholder) - 1 <= max_letter:
                    placeholder += words+" "
            else:
                final.append(placeholder)
                placeholder = words+" "
        final.append(placeholder)
        final = "\n".join(final)
        return final


if __name__ == "__main__":
    main = Standard()
    main.AddLabelWithText(tag="testing")
    print(main.Data)
    main.RemoveWithTag(tag = "testing")
    print(main.Data)
        
