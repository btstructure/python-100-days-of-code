from art import logo
from art import vs
from game_data import data 
import random



def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

print(logo)


account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)} ")
print(vs)
print(f"Compare B: {format_data(account_b)}  ")

choice = input("Who has more followers? Choose 'A' or 'B'." ).lower()

if choice == "A" and 