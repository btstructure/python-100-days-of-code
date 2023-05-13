from word_list import word_list
import random
import hangman_art

#chooses a random word from the word_list in word_list.py
chosen_word = random.choice(word_list)

#display will hold each letter in the chosen word
display = []
#the word length will be used to give each letter an index
word_length = len(chosen_word)

#adds an empty space "_" into display for each letter in the word 
for letter in range(word_length):
    display.append("_")

end_of_game = False

#the letters the user guessed, right or wrong, so they can't guess the same letter
guessed_letters = []
lives = 6

print(hangman_art.logo)

while not end_of_game:
    #a user entering a letter, and lowercases the user inpit
    user_guess = input("Guess a letter: ").lower()

    if user_guess in guessed_letters:
        print(f"You already guessed the letter '{user_guess}'.")
    else:
        guessed_letters.append(user_guess)
        if user_guess not in chosen_word:
            print(f"The letter '{user_guess}' is not in the word.")
            lives -= 1
            #prints the stages pictures by their index which depends on the value of lives
        else:
            #a for loop to go through each index in the word, if the letter is equal to the letter at the index, the letter will appear in the display
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == user_guess:
                    display[position] = letter
            
    print(hangman_art.stages[lives])            
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print("You lost")