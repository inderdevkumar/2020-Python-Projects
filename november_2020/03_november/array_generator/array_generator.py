
from datetime import datetime, timedelta

current_datetime= datetime.now().replace(microsecond= 0)
current_datetime_sec= int(current_datetime.timestamp())
user_input= int(input("Enter the day to be subtracted: "))

date_list = [current_datetime - timedelta(days=x) for x in range(user_input)]

last_datetime= date_list[len(date_list)-1]
last_datetime_sec= int(last_datetime.timestamp())

print(current_datetime_sec,  last_datetime_sec)

array_of_dates= []
for seconds in range(current_datetime_sec, last_datetime_sec, -5):
    
    value= datetime.fromtimestamp(seconds).strftime("%Y-%m-%d %H:%M:%S")
    array_of_dates.append(value)
    
print(array_of_dates)
