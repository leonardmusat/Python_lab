def ex6(lst):
    set1 = set(lst)
    num_unique = len(set1)
    num_duplicates = len(lst) - len(set1)

    return num_unique, num_duplicates


lst = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(ex6(lst))