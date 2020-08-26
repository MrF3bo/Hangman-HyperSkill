vowels = list("aeiou")

gibberish = input()

for letter in gibberish:
    if letter.isalpha():
        if letter in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break
