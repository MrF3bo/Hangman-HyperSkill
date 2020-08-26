scores = input().split()
# put your python code here

wrong = 0
correct = 0

for i in scores:
    if i == "I":
        wrong += 1
        if wrong >= 3:
            break
    else:
        correct += 1

if wrong >= 3:
    print("Game over")
    print(correct)
else:
    print("You won")
    print(correct)
