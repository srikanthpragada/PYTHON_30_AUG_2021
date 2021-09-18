def clean(s):
    return s.strip().upper()


a = [-10, 29, 11, 45, -50]
names = ['abc', 'xy', 'pqrs', 'aaaaa']
data = [' abc', '  Xy', 'pqrs', 'Aaaaa  ', 'bbb']

for n in sorted(a, key=abs):
    print(n)

for n in sorted(names, key=len):
    print(n)

for n in sorted(data, key=clean):
    print(n)
