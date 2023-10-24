
def group_by_rhyme(lst):
    new_list = []
    lsit_of_temp = []
    new_list_of_list = []
    for index in lst:
        if index[len(index)-2:] not in new_list:
            new_list.append(index[(len(index) - 2):])
    for index in new_list:
        for word in lst:
            if word[(len(word)-2):] == index:
                lsit_of_temp.append(word)
        new_list_of_list.append(lsit_of_temp)
        lsit_of_temp = []
    return  new_list_of_list


print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))

