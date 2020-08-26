word = input()
reverse = reversed(word)

if list(reverse) == list(word):
    print("Palindrome")
else:
    print("Not palindrome")
