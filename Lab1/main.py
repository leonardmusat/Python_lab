def cdm(arr):
    rez = 0
    counter = 0
    a = 1
    b = min(arr)
    while a <= b:
        for index in arr:
            if index % a == 0:
                counter += 1
        if counter == len(arr):
            rez = a
        a = a+1
        counter = 0
    return rez


#arr = [int(i) for i in input().split()]
#print('the gratest common divizor of your number is  ', cdm(arr))


# ________________________________________________________________________

def findVowels(string):
    count = 0
    vowels = "aeiou"
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count


# string = "I am not in the right place"
# print('the numer of vowels from your string is ', findVowels(string))

# _________________________________________________________________________


def countOccurence(string1, string2):
    positionInString1 = 0
    positionInString2 = 0
    count = 0
    while positionInString2 < len(string2):
        if string1[positionInString1] == string2[positionInString2]:
            positionInString2 += 1
            positionInString1 += 1
        else:
            if positionInString1 > 0:
                positionInString1 = 0
            else:
                positionInString1 = 0
                positionInString2 += 1
        if positionInString1 == len(string1):
            count += 1
            positionInString1 = 0
    return count


#print(countOccurence('adc', 'adcbacadcadcabc'))

# _________________________________________________________________________
def lowercase(string):
    string_nou = string[0].lower()
    for index in range(1, len(string)):
        if string[index].isupper():
            string_nou = string_nou + '_'
            string_nou = string_nou + string[index].lower()
        else:
            string_nou = string_nou + string[index]
    return string_nou


#print(lowercase("BunaSuntLeo"))

# _________________________________________________________________________

def matrixcover(matrix):
    num_rows = len(matrix) - 1
    num_colums = len(matrix[0]) - 1
    aux0 = 0
    aux1 = 1
    aux2 = -1
    string = ' '
    while num_colums != 0 or num_rows != 0:
        for index in range(aux0, num_colums + 1):
            string = string + matrix[aux0][index]
        for index in range(aux1, num_rows + 1):
            string = string + matrix[index][num_colums]
        for index in range(num_colums - 1, aux2, -1):
            string = string + matrix[num_rows][index]
        for index in range(num_rows - 1, aux1 - 1, -1):
            string = string + matrix[index][aux0]
        num_rows = num_rows - 1
        num_colums = num_colums - 1
        aux0 += 1
        aux1 += 1
        aux2 += 2
    return string


matrix = [
    ['V', 'R', 'E'],
    ['A', '_', 'A'],
    ['S', '_', 'U'],

]

#print(matrixcover(matrix))


# _________________________________________________________________________

def palindrom(number):
    a = number
    b = 0
    c = 0
    while a != 0:
        c = a % 10
        a = a // 10
        b = b * 10 + c
    if b == number:
        return True
    return False

# print(palindrom(19091))


# _________________________________________________________________________

def find_number(sentence):
    aux = ' '
    count_words = len(sentence.split())
    for index in range(0, count_words):
        string = sentence.split()[index]
        for char in string:
            if char.isdigit():
                aux = aux + char
    return aux


#print(find_number("Buna sunt 40sute sute eu"))


# _________________________________________________________________________

def count1 (nr):
    decimal = bin(nr)
    string = str(decimal)
    counter = 0
    for char in string:
        if char == '1':
            counter += 1
    return counter


#print(count1(24))


# _________________________________________________________________________

def count_words(prop):
    counter = 0
    for index in range(0, len(prop)):
        if prop[index] == ' ' and prop[index + 1] != ' ':
            counter += 1
    counter += 1
    return counter


#print(count_words("Aproape am terminat       tema"))


# _________________________________________________________________________

def maximum_count(string):
    dic = {
        "a": 0,
    }
    for char in string:
        if char in dic.keys():
            dic[char] = dic[char]+1
        else:
            dic[char] = 1
    return max(dic, key=dic.get)

#print(maximum_count("vreau acasa"))
