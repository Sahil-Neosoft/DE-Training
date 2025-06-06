import datetime
from datetime import date,time,datetime,timedelta

# Create a date object
dt=date(2025,6,8)
print(dt)

# Get today’s date
print(date.today())

#  Access year, month, and day
print(dt.year,dt.month,dt.day)
print("\n")

# Create and work with time objects
t=time(12,30,24)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print("\n")

#  Create and work with datetime objects
dt=datetime(2025,6,6,23,32)
print(dt)
print(dt.date())
print(dt.time())

#  Perform date arithmetic with timedelta
one_week=timedelta(days=7)
next_week=one_week+ dt
print(next_week)
yesterday=dt-timedelta(days=1)
print(yesterday)