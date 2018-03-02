while True:
    day = int(input('Day(0-6)? '))
    if 0 <= day <= 6:
        break
    else:
        print("Please input a number between 0~6!")
        continue
if 1 <= day <= 5:
    print("Go to work")
else:
    print("Sleep in")
