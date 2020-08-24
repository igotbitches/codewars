# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.


def generate_hashtag(s):
    if s == '':
        return False
    else:
        py_list = ['#']
        for i in s.title():
            if i.isalpha():
                py_list.append(i)
        x = ''.join(py_list)
        if len(x) > 140:
            return False
        else: 
            return x


"""крутая реализация"""
#def generate_hashtag(s):
    #output = "#"
    
    #for word in s.split():
       # output += word.capitalize()
    
   # return False if (len(s) == 0 or len(output) > 140) else output


print(generate_hashtag("Basic tests"))
print(generate_hashtag(''))
print(generate_hashtag('Do We have A Hashtag')[0])
print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
