# You are going to be given a word. Your job will be to make sure that each character in that word has the exact same number of occurrences. You will return true if it is valid, or false if it is not.
# For example:
# "abcabc" is a valid word because 'a' appears twice, 'b' appears twice, and'c' appears twice.
# "abcabcd" is NOT a valid word because 'a' appears twice, 'b' appears twice, 'c' appears twice, but 'd' only appears once! "123abc!" is a valid word because all of the characters only appear once in the word.


"""мой вариант"""
def validate_word(word):
    p_dict = {}
    p_list = []
    for i in word.lower():
        if i in p_dict:
            p_dict[i] += 1
        else:
            p_dict[i] = 1
    for value in p_dict.values():
        p_list.append(value)
    if len(set(p_list)) == 1:
        return True
    else:
        return False

"""бест практис"""
# from collections import Counter
#
#
# def validate_word(word):
#     return len(set(Counter(word.lower()).values())) == 1

print(validate_word('abcabc'))  # True
print(validate_word("Abcabc"))  # True
print(validate_word("AbcabcC"))  # False
print(validate_word("AbcCBa"))  # True
print(validate_word("pippi"))  # False
print(validate_word("?!?!?!"))  # True
print(validate_word("abc123"))  # True
print(validate_word("abcabcd"))  # False
print(validate_word("abc!abc!"))  # True
print(validate_word("abc:abc"))  # False
