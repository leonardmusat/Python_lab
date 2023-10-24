def longest(lst):
    contour = 0
    for item in lst:
        if len(item) > contour:
            contour = len(item)
    return contour


def mix_characters(lst):
    temp = []
    i = 0
    count = 0
    biggest = longest(lst)
    matrix = []

    while count != biggest:
        for item in lst:
            temp.append(item[i])
            if item.index(item[i]) == len(item)-1:
                item.append(None)
        i += 1
        count += 1
        matrix.append(tuple(temp))
        temp = []

    return matrix


list1 = [1,2,3]
list2 = [5,6]
list3 = ["a","b","c"]
list_final = [list1, list2, list3]


print(mix_characters(list_final))