# Write your code here
import random

words = ["python", "java", "kotlin", "javascript"]


print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
        lives = 8
        word = list(random.choice(words))
        hidden = list(("-" * len(word)))
        letters = list()
        while lives != 0:
            if hidden == word:
                print(f"\n{''.join(hidden)}")
                print("You guessed the word!")
                print("You survived!\n")
                break
            else:
                print(f"\n{''.join(hidden)}")
                guess = input("Input a letter: ")
                letters.append(guess)
                if len(guess) != 1:
                    print("You should input a single letter")
                elif guess.isascii() is False or guess.islower() is False:
                    print("It is not an ASCII lowercase letter")
                elif guess in word and guess not in hidden:
                    for i, letter in enumerate(word):
                        if guess == word[i]:
                            hidden[i] = guess
                elif letters.count(guess) > 1:
                    print("You already typed this letter")
                else:
                    lives -= 1
                    print("No such letter in the word")
        else:
            print("You are hanged!\n")
    elif menu == "exit":
        exit()
    else:
        continue
