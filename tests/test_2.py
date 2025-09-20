def x(a: list, b: list):
    list_1 = []
    for i in a:
        if i in b:
            list_1.append(i)
    return list_1


c = [1, 2, 3]
v = [2, 3, 4]
print(x([1, 2, 3], [2, 3, 4]))
print([x for x in v if x in c])