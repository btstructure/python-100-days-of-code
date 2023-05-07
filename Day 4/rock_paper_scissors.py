import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#My solution


user_choice_str = input("What is your choice? Type 'rock', 'paper', or 'scissors': ")
#Depending on what the user enters, their choice gets turned to the variable for comparison
if user_choice_str == 'rock':
    user_choice = rock
elif user_choice_str == 'paper':
    user_choice = paper
elif user_choice_str == 'scissors':
    user_choice = scissors
else:
    print("Invalid input. Please try again.")
    exit()

choices = [rock, paper, scissors]
computer_choice = random.choice(choices)


if user_choice == computer_choice:
    print(user_choice)
    print(computer_choice)
    print("Tie!")
elif user_choice == 'rock' and computer_choice == scissors:
    print(user_choice)
    print(computer_choice)
    print("You win rock beats scissors!")
elif user_choice == 'paper' and computer_choice == rock:
    print(user_choice)
    print(computer_choice)
    print("You win paper beats rock!")
elif user_choice == 'scissors' and computer_choice == paper:
    print(user_choice)
    print(computer_choice)
    print("You win scissors beats paper!")
else:
    print(user_choice)
    print(computer_choice)
    print("Computer won!")



# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")