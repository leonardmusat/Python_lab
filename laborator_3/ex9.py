def my_function(*pos, **keyword):
    counter = 0
    for char in pos:
        for value in keyword.values():
            if char == value:
                counter = counter + 1
    return counter

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))