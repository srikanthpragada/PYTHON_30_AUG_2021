def startsWithUpper(s):
    return s[0].isupper()


def containsUpper(s):
    for c in s:
        if c.isupper():
            return True

    return False


names = ['Python', 'java', 'C', 'C#', 'TypeScipt', 'ruST']

# for n in filter(startsWithUpper, names):
#     print(n)

# for n in filter(containsUpper, names):
#     print(n)

names = ['JAVA', 'Python', 'C', 'JavaScript']

for n in filter(str.isupper, names):
    print(n)
