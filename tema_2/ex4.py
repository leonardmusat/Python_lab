def muzic(string, list, integer):
    notes = string.split()
    rez = []
    rez.append(notes[integer])
    for i in list:
        rez.append(notes[(integer + i)%5])
        integer = integer + i
    return rez


print(muzic("do re mi fa sol", [1, -3, 4, 2], 2))


