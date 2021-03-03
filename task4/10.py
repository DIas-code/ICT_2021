import datetime
from datetime import timedelta 
date = input()
currdate = datetime.to_datetime(date)
nextday = currdate + timedelta(days = 1)
print(nextday)
