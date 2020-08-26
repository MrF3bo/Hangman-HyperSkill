# put your python code here

num1 = float(input())
num2 = float(input())
op = input()

if num2 == 0 and op in ["mod", "div", "/"]:
    print("Division by 0!")
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "mod":
    print(num1 % num2)
elif op == "pow":
    print(num1 ** num2)
elif op == "div":
    print(num1 // num2)
