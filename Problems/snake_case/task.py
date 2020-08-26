word = input()
snake_word = ""

for letter in word:
    if letter.isupper():
        snake_word += f"_{letter.lower()}"
    else:
        snake_word += letter

print(snake_word)
