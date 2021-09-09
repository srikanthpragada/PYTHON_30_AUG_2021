names = []

while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    names.append(name)
# Sort the list and print names
for name in sorted(names):
    print(name)
