from coffee_menu import MENU

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte, cappucino): ")
    if choice == "off":
        is_on = False