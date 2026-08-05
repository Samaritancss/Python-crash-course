import datetime

#access today's date
date = datetime.date(2025, 8, 9)
today = datetime.date.today()
print(today)

#access time now
time = datetime.time(11, 14, 10)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S  %m-%d-%Y")
print(now)

#target date maybe for alarm or event

target_datetime = datetime.datetime(2030, 10, 16, 13, 9, 2) 
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

