from datetime import datetime;

currHour = datetime.now().hour
print("Current Hour: ",currHour)

if(0<=currHour<12):
    print("Good Morning")
elif(12<=currHour<16):
    print("Good Afternoon")
elif(16<=currHour<20):
    print("Good evening")
else:
    print("Good night")