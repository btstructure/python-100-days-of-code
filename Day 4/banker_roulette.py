# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
#when giving names in a input with commas in between, the split will create a list of the individial names and separate them by comma
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#using random to get a random index. you subtract the length by one because an index starts at 0, but the length does not
random = random.randint(0, len(names) - 1)
#within the name list, a random index is chosen
person_chosen = names[random]
print(f"{person_chosen} is going to buy the meal today!")