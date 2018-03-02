while True:
    day = int(input('Day(0-6)? '))
    if 0 <= day <= 6:
        break
    else:
        print("Please input a number between 0~6!")
        continue
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Saturday")
