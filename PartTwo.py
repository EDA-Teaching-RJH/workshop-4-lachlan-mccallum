d = input("what drink would you like? ").lower()

if d == "coffe":
    x = int(0)
    while x < 75:
        y = int(input("input a coin. "))

        x = x + y

    print ("here is your coffee. :)")
elif d == "tea":
    x = int(0)
    while x < 50:
        y = int(input("input a coin. "))

        x = x + y

    print ("here is your tea. :)")
elif d == "hot chocolate":
    x = int(0)
    while x < 100:
        y = int(input("input a coin. "))

        x = x + y

    print ("here is your hot chocolate. :)")
else:
    print ("sorry we dont serve that here.")