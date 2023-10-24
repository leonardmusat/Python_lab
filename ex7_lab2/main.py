def is_palindrom(n):
    a = n
    b = 0
    c = 0
    while a != 0:
        c = a % 10
        a = a // 10
        b = b * 10 + c
    if b == n:
        return True
    return False


def compute_palinfrom(lst):
    rez = []
    count = 0
    for index in lst:
        if is_palindrom(index):
            rez.append(index)
            count = count+1
    temp = max(rez)
    return (count,temp)


print(compute_palinfrom([111, 1221, 12, 45, 66]))
