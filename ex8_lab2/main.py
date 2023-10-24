def ASCII(integer, lst, boolean):
    letter = []
    if boolean:
        for char in lst:
            letter = letter + [char2 for char2 in char if ord(char2) % integer == 0]
    else:
        for char in lst:
            letter = letter + [char2 for char2 in char if ord(char2) % integer != 0]
    return letter


print(ASCII(2, ["test", "hello", "lab002"],False))
