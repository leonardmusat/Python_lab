def compare_dictionaries(dict1, dict2):
    for i, j in zip(dict1.keys(), dict2.keys()): #folosesc zip() pentru a itera prin 2 liste, formate din cheile dictionarelor, in acelasi timp
        if i != j:
            return False

        neutru1 = dict1[i]
        neutru2 = dict2[j]

        if type(neutru1) != type(neutru2):
            return False

        if isinstance(neutru1, dict):
            if compare_dictionaries(neutru1, neutru2) != True:
                return False
        elif isinstance(neutru1, list):
            for char1, char2 in zip(neutru1, neutru2):
                if (char1 != char2):
                    return False
        elif isinstance(neutru1, set):
            if neutru1 & neutru2 != neutru1:
                return False
        elif neutru1 != neutru2:
            return False
    return True


dict_a = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
dict_b = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
result = compare_dictionaries(dict_a, dict_b)
print(result)