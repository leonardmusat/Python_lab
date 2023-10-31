def ex2(string):
    string = string.lower()
    dict = {}
    for char in string:
        if char in dict.keys():
            dict[char] = dict[char] + 1
        else:
            dict.update({char: 1})
    return dict


print(ex2("Ana has apples."))
