student = int(input())
maximum = int(input())

if student/maximum * 100 >= 90:
    print("A")
elif student/maximum * 100 >= 80:
    print("B")
elif student/maximum * 100 >= 70:
    print("C")
elif student/maximum * 100 >= 60:
    print("D")
else:
    print("F")
