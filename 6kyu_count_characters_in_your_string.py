# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    py_dict = {}
    for i in string:
        if i not in py_dict:
            py_dict[i] = 1
        else:
            py_dict[i] += 1
    
    return py_dict


print(count('abaserba'))



"""ещё один способ через импорт"""

#from collections import Counter

#def count(string):
#    return Counter(string)