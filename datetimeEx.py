import datetime


# String to date_time


def string_to_datetime(input):
    formate = "%b %d %Y %I:%M%p"
    date = datetime.datetime.strptime(input, formate)

    return date


input = "Oct 02 2000 10:00AM"
print(string_to_datetime(input))
