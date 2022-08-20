print("Welcome to the tip Calculator ")

bill = float(input("What was the total bill? $"))
tip = float(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))
numberOfPeople = int(input("How many people to split the bill? "))

tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount
billPerPeople = totalBill / numberOfPeople
finalAmount = round(billPerPeople, 2)


print(f"Each person should pay : ${finalAmount}")
