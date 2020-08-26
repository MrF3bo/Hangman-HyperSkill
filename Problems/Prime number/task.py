number = int(input())
count = 0

if number > 1:
    for i in range(2, number + 1):
        if number % i == 0:
            count += 1
            if count > 1:
                print("This number is not prime")
                break
    else:
        print("This number is prime")
else:
    print("This number is not prime")
