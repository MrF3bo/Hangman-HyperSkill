n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

for number in numbers:
    if number % 7 == 0:
        print(number ** 2)
