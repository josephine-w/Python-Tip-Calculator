######
# Tip Calculator
# Josephine Widjaja
# 09/01/2021

import time

# Greeting
print("Welcome to the tip calculator!")

time.sleep(2)

print()
print("This calculator will help you determine how much you should tip based on your inputs.")
print ()

time.sleep(2.5)

# Input bill
bill = float(input("Please enter your bill: $"))

# Determine if order is dine-in or take-out
validType = False

while not validType:
    typeOfTip = input("Is your order dine-in (D) or take-out (T)?: ")

    if typeOfTip.upper() in ("D","T"):
        validType = True

    else:
        print("Please enter 'D' for dine-in or 'T' for take-out.")
        print()

# Calculates the tip given dine-in
def dineintip ():
    servicelevel = input("How was the service? (bad, mediocre, good): ")

    if servicelevel.lower() == 'bad':
        lowerTipAmount = 0
        higherTipAmount = 0.05

    elif servicelevel.lower() == 'mediocre':
        lowerTipAmount = 0.1
        higherTipAmount = 0.12

    elif servicelevel.lower() == 'good':
        lowerTipAmount = 0.15
        higherTipAmount = 0.2

    else: print("Please enter 'bad','mediocre', or 'good': ")

    return lowerTipAmount,higherTipAmount

# Calculates tip given take-out
def takeouttip():
    lowerTipAmount = 0.05
    higherTipAmount = 0.1

    return lowerTipAmount, higherTipAmount

# Main tip calculation function
def calculatetip(typeoftip):
    if typeoftip.upper() == "D":
        return dineintip()
    else: return takeouttip()

tip = calculatetip(typeOfTip)

lowerTip = "{:.2f}".format(bill*tip[0])
higherTip = "{:.2f}".format(bill*tip[1])
print()

print ("You should tip between " + lowerTip + " and " + higherTip)

time.sleep(2)
print()

x = input("Press the close button to exit.")