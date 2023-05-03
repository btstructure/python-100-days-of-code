bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15?"))
split = int(input("How many people split the bill?"))

calculation = (bill + (bill * (tip/100))) / split

print(f"Each person should pay ${calculation}")