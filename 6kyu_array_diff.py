"""числа, которые есть в списке B, должны удалиться из списка A"""

def array_diff(a, b):
    data =[]
    for i in a:
        if i not in b:
            data.append(i)
    return data

print(array_diff([1,2], [1]))

