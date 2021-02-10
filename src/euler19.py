print('project euler problem 19')

def isLeapYear(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def nextDay(curDay):
        month = curDay.month
        day = curDay.day
        year = curDay.year
        leap = isLeapYear(year)
        nextDay = { day: -1, month: -1, year: -1 }
        if month == 2:
                if leap:
                        if day == 29:
                                month = 3
                                day = 1
                        else:
                                day += 1
                else:
                        if day == 28:
                                month = 3
                                day = 1
                        else:
                                day += 1

dayOfWeek = 0
curMonth = 1

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?