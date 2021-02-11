print('project euler problem 19')

def isLeapYear(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def getNextDay(day):
        if day == 7:
                day = 1
        else:
                day += 1
        return day

def nextDay(curDay):
        month = curDay["month"]
        day = curDay["day"]
        year = curDay["year"]
        dayOfWeek = curDay["dayOfWeek"]
        leap = isLeapYear(year)
        nextDay = { "day": -1, "month": -1, "year": -1, "dayOfWeek": -1 }
        nextDay["day"] = day
        nextDay["month"] = month
        nextDay["year"] = year
        nextDay["dayOfWeek"] = getNextDay(dayOfWeek)
        if month == 2:
                if leap:
                        if day == 29:
                                nextDay["month"] = 3
                                nextDay["day"] = 1
                        else:
                                nextDay["day"] = day + 1
                else:
                        if day == 28:
                                nextDay["month"] = 3
                                nextDay["day"] = 1
                        else:
                                nextDay["day"] = day + 1
        elif month in [9, 4, 6, 11]:
                if day == 30:
                        nextDay["month"] = month + 1
                        nextDay["day"] = 1
                else:
                        nextDay["day"] = day + 1
        elif month == 12: 
                if day == 31:
                        nextDay["month"] = 1
                        nextDay["day"] = 1
                        nextDay["year"] = year + 1
                        print("year is now ", nextDay["year"])
                else: 
                        nextDay["day"] = day + 1
        else:
                if day == 31:
                        nextDay["month"] = month + 1
                        print("month is now ", nextDay)
                        nextDay["day"] = 1
                else:
                        nextDay["day"] = day + 1
        return nextDay

curDay = {}
curDay["month"] = 1
curDay["day"] = 1
curDay["year"] = 1900
curDay["dayOfWeek"] = 1

day = curDay
count = 0
while day["year"] < 2001:
        day = nextDay(day)
        if day["year"] >= 1901:
                if day["dayOfWeek"] == 7 and day["day"] == 1:
                        count += 1

print("count is ", count)
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?