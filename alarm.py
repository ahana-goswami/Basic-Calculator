import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

    if current_time == alarm_time:
        print("Wake up! Alarm ringing!")
        break

    time.sleep(1)