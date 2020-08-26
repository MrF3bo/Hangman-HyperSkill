# put your python code here

number = int(input())
square = number ** 2
sums = number

if number == 0:
    print(number)
else:
    while True:
        number = int(input())
        sums += number
        square += number ** 2
        if sums == 0:
            print(square)
            break
