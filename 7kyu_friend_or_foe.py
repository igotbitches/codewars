# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]


x = ["Ryan", "Kieran", "Mark", "Jason"]


def friend(x):
    new_list = []
    for j in x:
        if len(j) > 4 or len(j) < 4:
            continue
        else:
            new_list.append(j)
    return new_list


print(friend(x))
