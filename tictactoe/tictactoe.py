area = ["1.1", "1.2", "1.3", "2.1", "2.2", "2.3", "3.1", "3.2", "3.3"]
a = f"| {area[0]} | {area[1]} | {area[2]} |" \
    f"\n| {area[3]} | {area[4]} | {area[5]} |" \
    f"\n| {area[6]} | {area[7]} | {area[8]} |"
print(a)
n = 0
while True:
    coordinates_x = area.index(str(input("Enter coordinates X\n>")))
    area[coordinates_x] = " X "
    a = f"| {area[0]} | {area[1]} | {area[2]} |" \
        f"\n| {area[3]} | {area[4]} | {area[5]} |" \
        f"\n| {area[6]} | {area[7]} | {area[8]} |"
    print(a)
    dict_area = dict.fromkeys(area)
    n += 1
    c = dict_area[" X "] = n
    if dict_area[" X "] == 5:
        print("DEAD HEAT")
        break
    wins = [(area[0:3]), (area[3:6]), (area[6:9]), (area[0], area[3], area[6]),
            (area[1], area[4], area[7]), (area[2], area[5], area[8]),
            (area[0], area[4], area[8]), (area[2], area[4], area[6])]
    if (" X ", " X ", " X ") in wins or [" X ", " X ", " X "] in wins:
        print("X win")
        break
    coordinates_o = area.index(str(input("Enter coordinates 0\n>")))
    area[coordinates_o] = " 0 "
    a = f"| {area[0]} | {area[1]} | {area[2]} |" \
        f"\n| {area[3]} | {area[4]} | {area[5]} |" \
        f"\n| {area[6]} | {area[7]} | {area[8]} |"
    print(a)
    wins = [(area[0:3]), (area[3:6]), (area[6:9]), (area[0], area[3], area[6]),
            (area[1], area[4], area[7]), (area[2], area[5], area[8]),
            (area[0], area[4], area[8]), (area[2], area[4], area[6])]
    if (" 0 ", " 0 ", " 0 ") in wins or [" 0 ", " 0 ", " 0 "] in wins:
        print("0 win")
        break
