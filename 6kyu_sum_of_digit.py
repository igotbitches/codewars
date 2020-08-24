# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
# Examples:
# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6

"""my decision"""
def digital_root(n):
    x = sum(map(int, str(n)))
    if len(str(x)) != 1:
        y = sum(map(int, str(x)))
        if len(str(y)) != 1:
            z = sum(map(int, str(y)))
            return z
        return y
    else:
        return x


"""easy desicion"""

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int, str(n))))


"""best but difficult for understanding"""

# def digital_root(n):
#     return n % 9 or n and 9


"""not bad decision also"""

# def digital_root(n):
#     root = 0
#     for d in str(n):
#         root += int(d)
#     if len(str(root)) > 1:
#         root = digital_root(root)
#     return root
#
# print(digital_root(493193))