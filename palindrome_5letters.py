def palindrome(data):
    spin_words = data.split(" ")

    for i in range(len(spin_words)):
        if len(spin_words[i]) >= 5:
            spin_words[i] = spin_words[i][::-1]
            print(spin_words[i])
    return ' '.join(spin_words)


data = 'Welcome'
print(f'spin_word ("{data}"), {palindrome(data)}')


