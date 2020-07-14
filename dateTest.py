from datetime import datetime, timedelta
from dateutil import tz, parser
from dateutil.relativedelta import relativedelta

now = datetime.now()
print(now)
# print(now.tzname())

london_tz = tz.gettz("Europe/London")
now_london = datetime.now(tz=london_tz)
print("the london time is %s" % (now_london) )
print(now_london.tzname())

PYCON_DATE = parser.parse('MAY 12, 2021 8:00AM') # Naivedate
PYCON_DATE = PYCON_DATE.replace(tzinfo = tz.gettz('America/New_York')) # Awaredate
print(PYCON_DATE, PYCON_DATE.tzname())
now_tz = datetime.now(tz=tz.tzlocal())
countdown = PYCON_DATE - now_tz
print(f"Countdown to PyCon US 2021 : {countdown}")

day_change = timedelta(days=+1)

tomorrow = now + day_change
print (f" Tomorrow days is {tomorrow}")

now2 = datetime.now()
tomorrow_delta = datetime(2020, 5, 18, 17, 22, 46, 349349)
time_delta = relativedelta(now2, tomorrow_delta)
print(time_delta)


delta = relativedelta(years=+5, months=+1, days=+3, hours=-4, minutes=-30)
print(now2 + delta)

# delta countdown

countdown_delta = relativedelta(PYCON_DATE, now_tz)
print(countdown_delta)
