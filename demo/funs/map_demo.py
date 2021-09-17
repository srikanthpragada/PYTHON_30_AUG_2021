names = ['Python  ', 'java', 'C', 'C#', '  TypeScipt  ', '   ruST']

for n in map(len, names):
    print(n)

for n in map(str.strip, names):
    print(n)
