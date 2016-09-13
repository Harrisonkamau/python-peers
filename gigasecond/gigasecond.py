import time
from datetime import date, datetime, timedelta
import calendar


def add_gigasecond(year, month, day):

    date_now = time.strftime("%Y-%m-%d")
    birth_date = date(year, month, day)
    giga_anniversary = birth_date+timedelta(seconds=10**9)
    weekday = calendar.day_name[giga_anniversary.weekday()]

    d1 = datetime.strptime(str(giga_anniversary), "%Y-%m-%d")
    d2 = datetime.strptime(str(date_now), "%Y-%m-%d")
    days_left = str(abs((d2 - d1).days))

    return [giga_anniversary.isoformat(), weekday, days_left+' days left']

print add_gigasecond(1988, 5, 15)
print add_gigasecond(2015, 2, 17)