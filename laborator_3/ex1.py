def operation(a, b):
    set_a = set(a)
    set_b = set(b)

    intersection = set_a.intersection(set_b)
    reunion = set_a.union(set_b)
    dif1 = set_a.difference(set_b)
    dif2 = set_b.difference(set_a)

    rez = [intersection, reunion, dif1, dif2]
    return rez


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(operation(a, b))