ls = ['a','o','u','e','i','A','E','I','O','U']
s = input()
s = s.split()
for i in range(len(s)):
    if s[i][0] in ls:
        print(s[i])
