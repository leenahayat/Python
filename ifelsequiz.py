import time

timestamp = time.strftime("%H:%M:%S")


print("Current time:", timestamp)

hour = int(time.strftime('%H'))

if (hour < 12):
    print("Good Morning")
elif (hour < 18):
    print("Good Evening")
else:
    print("Good Night")
