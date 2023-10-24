def order(lst):
    rez = sorted(lst, key=lambda x: x[1][2])
    return rez


lst = [('abc', 'bcd'), ('abc', 'zza'), ('aac', 'bbb')]
print(order(lst))