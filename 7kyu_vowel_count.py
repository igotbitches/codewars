input_str = input('Say something: ')
def get_count(input_str):
    num_vowels = 0
    vowels = 'aeiou'
    for i in input_str:
        if i.lower() in vowels:
            num_vowels += 1
    return num_vowels

print(get_count(input_str))