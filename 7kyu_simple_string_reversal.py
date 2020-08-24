"""solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo".
-- However, there is a space after the first three characters, hence "edo cruo"""

def solve(s):
    x = s[::-1]
    z = []
    for j in x:
        if j == " ":
            pass
        else:
            z.append(j)
    for i in range(len(s)):
        if s[i] == ' ':
            z.insert(i, s[i])
    return ''.join(z)


print(solve("codewars")) #"srawedoc"
print(solve("your code rocks")) #"skco redo cruoy"
print(solve("i love codewars")) #"s rawe docevoli"

