minimum = float(input())

while True:
    number = input()
    if number == ".":
        break
    elif float(number) < minimum:
        minimum = float(number)

print(minimum)
