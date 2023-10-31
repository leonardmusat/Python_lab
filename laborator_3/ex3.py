def compare(dict1, dict2):
    list1 = list(dict1.keys())
    list2 = list(dict2.keys())
    set1 = set(list1)
    set2 = set(list2)

    if set1.issubset(set2) and set2.issubset(set1):
        x1 = dict1.values()
        x = set(x1)
        y1 = dict2.values()
        y = set(y1)
        if not(x.issubset(y) and y.issubset(x)):
            return False
    return True


dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict2 = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print(compare(dict1, dict2))
