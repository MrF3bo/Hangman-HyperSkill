max_cafe = ""
max_cats = 0

while True:
    cafe = input()
    cafe_list = list(cafe.split())
    if cafe == "MEOW":
        break
    elif int(cafe_list[1]) > max_cats:
        max_cafe = cafe_list[0]
        max_cats = int(cafe_list[1])

print(max_cafe)
