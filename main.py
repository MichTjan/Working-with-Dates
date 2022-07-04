"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

#days in month function
def days_in_month(year, month):
    """
    This function takes two integers: a year and a month, then returns the 
    number of days in the given month.
    """
    
    #calculates the number of days in the given month
    if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <= 11):
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, month + 1, 1)
        return (date2 - date1).days
    elif (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (month == 12):
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year + 1, month, 1)
        return (date2 - date1).days
    else: 
        return False

#is valid date function 
def is_valid_date(year, month, day):
    """
    This function takes three integers: a year, a month, and a day, then returns
    the validity of the date. True if valid, false if otherwise
    """
    #validates the year, month, and day inputs 
    if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <= 12) and (1 <= day <= int(days_in_month(year, month))):
        return True
    else:
        return False

#days between function
def days_between(year1, month1, day1, year2, month2, day2):
    """
    This function takes six integers: year1, month1, day1, year2, month2, and day2, then returns
    the number of days between the two dates, (year1, month1, day1) and (year2, month2, day2)
    if the first date is later than the second date or invalid, returns 0
    """
    #calculates the number of days between the two dates
    if bool(is_valid_date(year1, month1, day1)) and bool(is_valid_date(year2, month2, day2)):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date2 > date1:
            return (date2 - date1).days
        else:
            return 0
    else:
        return 0

#age in days function
def age_in_days(year, month, day):
    """
    This function takes three integers: year, month, and day, then returns the age of a person
    with the input birthday as of today. If the input date is invalid or in the future, returns 0
    """
    #calculates a person's age from the input birthday as of today
    if bool(is_valid_date(year, month, day)):
        todays_date = datetime.date.today() 
        birthday_date = datetime.date(year, month, day)
        if todays_date > birthday_date:
            return (todays_date - birthday_date).days
        else:
            return 0
    return 0