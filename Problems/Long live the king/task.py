column = int(input())
row = int(input())

corner = [1, 8]
side = [2, 3, 4, 5, 6, 7]

if column in corner:
    if row in corner:
        print("3")
    elif row in side:
        print("5")
elif (row in corner) and (column in side):
    print("5")
else:
    print("8")
