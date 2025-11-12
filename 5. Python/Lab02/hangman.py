# * Word guessing game (hangman)
#    -  A list of words will be hardcoded in your program, out of which the interpreter will
#    -  choose 1 random word.
#    -  The user first must input their names
#    -  Ask the user to guess any alphabet. If the random word  contains that alphabet, it
#    -  will be shown as the output(with correct placement)
#    -  Else the program will ask you to guess another alphabet.
#    -  Give 7 turns maximum to guess the complete word

import random

words = ['python', 'apple', 'match', 'sharaf', 'ahmed', 'elsherbiny', 'iti']
word = random.choice(words)
display = ["_"] * len(word)
turns = 7

name = input("Enter your name: ").strip()
print(f"Welcome, {name}!")
print("Guess the word:", " ".join(display))

while turns > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only")
        continue
    
    found = False
    for i, ch in enumerate(word):
        if ch == guess and display[i] == "_":
            display[i] = guess
            found = True
            break

    if found:
        print("Correct:", " ".join(display))
    else:
        turns -= 1
        print(f"Wrong, You have {turns} turns left")
        print(" ".join(display))

if "_" not in display:
    print(f"Congrats {name}! You guessed the word: {word}")
else:
    print(f"Game over, The word was: {word}")
