if __name__ != "__main__":
    from components.Standard import Standard

class Reminder():
    __Delim = "nITF0CxrEbNZa1R9Iwgpgw35jzNpk7Qpg6TZCygrZZvwa3xjN6TCo9AlWRw6XlOa1oyfY0aSAeUbk18vhD91ZwaqMh9nPD523G9M"
    __ReminderList = []

    def Run(self):
        standard = Standard()
        self.LoadReminders()
        string = ""
        for i in self.__ReminderList:
            string += "- {}\n".format(standard.FormatSentence(i, 20))
        standard.UpdateTextByTag("reminders", string)
        standard.Commit()

    def RunSpecial(self):
        pass

    def AddReminder(self, reminder):
        self.__ReminderList.append(reminder)
    
    def RemoveReminder(self, index):
        self.__ReminderList.pop(index)
    
    def ReplaceReminder(self, index, reminder):
        self.__ReminderList[index] = reminder
    
    def SaveReminders(self):
        result = self.__Delim.join(self.__ReminderList)
        if __name__ == "__main__":
            file = open("reminders.txt", "w")
        else:
            file = open("components/reminders.txt","w")
        file.write(result)
        file.close()
    
    def LoadReminders(self):
        if __name__ == "__main__":
            file = open("reminders.txt", "r")
        else:
            file = open("components/reminders.txt","r")
        result = file.read()
        file.close()
        self.__ReminderList = result.split(self.__Delim)


if __name__ == "__main__":
    a = Reminder()
    a.Run()
