from word_list import word_list
import random

#chooses a random word from the word_list in word_list.py
chosen_word = random.choice(word_list)

#a user entering a letter, and lowercases the user inpit



#display will hold each letter in the chosen word
display = []
#the word length will be used to give each letter an index
word_length = len(chosen_word)

#adds an empty space "_" into display for each letter in the word 
for letter in range(word_length):
    display.append("_")

end_of_game = False

tries = 6

#a for loop to go through each index in the word, if the letter is equal to the letter at the index, the letter will appear in the display
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
        else:
            tries -= 1
            
                
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    elif tries == 0:
        end_of_game = True
        print("You lost")