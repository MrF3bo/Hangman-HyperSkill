TIME = 10.5

new_time = input()

if TIME + int(new_time) >= 24:
    print("Wednesday")
elif TIME + int(new_time) < 0:
    print("Monday")
else:
    print("Tuesday")
