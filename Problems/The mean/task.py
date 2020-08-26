sums = 0
count = 0
while True:
    number = input()
    if number == ".":
        break
    else:
        sums += int(number)
        count += 1

print(sums / count)
