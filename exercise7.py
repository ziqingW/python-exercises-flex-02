total = float(input("Total bill amount? "))
service = ""
tipPercent = 0
while True:
    service = input("Level of service? ")
    if service == "good":
        tipPercent = 0.2
        break
    elif service == "fair":
        tipPercent = 0.15
        break
    elif service == "bad":
        tipPercent = 0.1
        break
    else:
        print("Choose a service level from \"good, fair and bad\" ")
        continue
tipAmount = total * tipPercent
totalAmount = total + tipAmount
print("Tip amount: ${:.2f}".format(tipAmount))
print("Total amount: ${:.2f}".format(totalAmount))