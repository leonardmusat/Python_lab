def intersected(lst1, lst2):
    rez = []
    for i in lst1:
        if i in lst2:
           rez.append(i)
    return rez


def reunited(lst1, lst2):
    rez = []
    for i in lst1:
        if i not in rez:
            rez.append(i)
    for i in lst2:
        if i not in rez:
            rez.append(i)
    return rez


def minus(lst1, lst2):
    for i in lst1:
        if i in lst2:
         lst2.remove(i)
    return lst2


def operation(par, lst1, lst2):
    final_rez = []
    if par == 'A':
        final_rez = intersected(lst1, lst2)
    elif par == 'U':
        final_rez = reunited(lst1, lst2)
    elif par == "-":
        final_rez = minus(lst2, lst1)
    elif par == "@":
        final_rez = minus(lst1, lst2)
    return final_rez


lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
print(operation('A', lst1, lst2))
print(operation('U', lst1, lst2))
print(operation('-', lst1, lst2))
print(operation('@', lst1, lst2))
