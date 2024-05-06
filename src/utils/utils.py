import datetime


def mileseconds_to_date(milliseconds):
    start = datetime.datetime(1970, 1, 1)
    date_time = start + datetime.timedelta(milliseconds=milliseconds)
    return date_time


if __name__ == "__main__":
    seconds = 1234567890
    date_time = mileseconds_to_date(seconds)
    print("Date and time:", date_time)
