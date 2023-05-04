# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Hint
# The lower() function changes all the letters in a string to lowercase.
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

# The count() function will give you the number of times a letter occurs in a string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#lower casing the names and concatenating the strings
lower_name1 = name1.lower()
lower_name2 = name2.lower()
names_together = lower_name1 + lower_name2

#counting the letters for true
count_of_true_letters = names_together.count("t") + names_together.count("r") + names_together.count("u") + names_together.count("e")
#counting the letters for love
count_of_love_letters = names_together.count("l") + names_together.count("o") + names_together.count("v") + names_together.count("e") 

#the numbers aren't add by int, but the number for count_of_true_letters + count_of_love_letters. It's the value of the two strings together
str_value_together = str(count_of_true_letters) + str(count_of_love_letters)
#convert the total number to int to make the comparisons
names_count_total_int = int(str_value_together)

#conditional
if names_count_total_int < 10 or names_count_total_int > 90:
    print(f"Your score is {names_count_total_int}, you go together like coke and mentos.")
elif names_count_total_int >= 40 and names_count_total_int <= 50:
    print(f"Your score is {names_count_total_int}, you are alright together.")
else:
    print(f"Your score is {names_count_total_int}.")