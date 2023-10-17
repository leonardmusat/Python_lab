def muzic(string, list, integer):
    notes = string.split()
    rez = []
    rez.append(notes[integer])
    for i in list:
        rez.append(notes[integer + i])
        integer = integer + i
    return rez


print(muzic("do re mi fa sol la si do", [1, 2, -3, -2, 1], 2))


