"""In this module practice with datetime"""
import datetime


# String to date_time


def string_to_datetime(str_date):
    """This function used to convert string formate of date, time to datetime format"""
    formate = "%b %d %Y %I:%M%p"
    date = datetime.datetime.strptime(str_date, formate)

    return date


INPUT = "Oct 02 2000 10:00AM"
print(string_to_datetime(INPUT))
