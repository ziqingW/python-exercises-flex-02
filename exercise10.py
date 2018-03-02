coin = 0
while True:
    print("You have {} coins.".format(coin))
    answer = ""
    while answer not in ["yes", "no"]:
        answer = input("Do you want another? ")
    if answer == "yes":
        coin += 1
    else:
        break
print("Bye")