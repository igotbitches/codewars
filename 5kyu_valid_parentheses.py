"""Допустимые скобки (правильные скобочные последовательности)"""

"""лучшее для меня решение"""

def valid_parentheses(string):
    counter = 0
    for i in string:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

"""хорошее врешение, лучшая практика"""
# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False

"""моё решение"""
# def valid_parentheses(string):
#     if len(string) <= 100 and len(string) >= 0:
#         first = ['(', '[', '{', '<']
#         second = [')', ']', '}', '>']
#         if string == "":
#             return True
#         counter = 0
#         for i in string:
#             if i in first:
#                 counter += 1
#             if i in second:
#                 counter -= 1
#             if counter == -1:
#                 return False
#                 break
#         if counter == 0:
#             return True
#         else:
#             return False