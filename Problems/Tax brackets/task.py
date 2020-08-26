income = float(input())
tax = 0

if income >= 132407:
    tax = 0.28
elif income >= 42708:
    tax = 0.25
elif income >= 15528:
    tax = 0.15
else:
    tax = 0

calculated_tax = income * tax

print(f"The tax for {income:.0f} is {tax * 100:.0f}%. That is {round(calculated_tax)} dollars!")
