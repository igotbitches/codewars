import math

def is_square(n):
    if n <= -1:
        print('Negative number cannot be square numbers')
    elif math.sqrt(n).is_integer():
        return True
    return False # fix me

print(is_square(-1))