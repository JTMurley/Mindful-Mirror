import datetime
if __name__ != "__main__":
    from components.Standard import Standard

class Time():
    __Now = datetime.datetime.now()
    def Run(self):
        pass

    def RunSpecial(self):
        standard = Standard()
        result = "{}:{} {}".format(self.HourTwelve(),self.Minute(),self.AmPm())
        standard.UpdateTextByTag("timecurrenttime", result)
        result = "{} {} {}".format(self.Day(),self.MonthWord(),self.Year())
        standard.UpdateTextByTag("timecurrentdate", result)
        standard.Commit()

    def Now(self):
        """Get the current full time in string"""
        return str(self.__Now)

    def Hour(self):
        """Get the current hour in string"""
        hour = str(self.__Now.hour)
        return self._FormatText(hour)
    
    def HourTwelve(self):
        """Get the current hour in 12 hours format"""
        hour = int(self.Hour())
        if hour > 12:
            return self._FormatText(str(hour-12))
        else:
            return str(hour)
    
    def AmPm(self):
        if int(self.Hour()) > 12:
            return "PM"
        else:
            return "AM"

    def Minute(self):
        """Get the current minute in string"""
        minute = str(self.__Now.minute)
        return self._FormatText(minute)
    
    def Year(self):
        """Get the current year in string"""
        return str(self.__Now.year)

    def Month(self):
        """Get the current month in string"""
        month = str(self.__Now.month())
        return self._FormatText(month)
    
    def MonthWord(self):
        return self.__Now.strftime("%B")
    
    def Day(self):
        """Get the current day in string"""
        day = str(self.__Now.day)
        return self._FormatText(day)
    
    def _FormatText(self, string):
        if len(string) == 1:
            return "0"+string
        else:
            return string

if __name__ == "__main__":
    a = Time()
    print("{} {} {}".format(a.Day(), a.MonthWord(), a.Year()))
