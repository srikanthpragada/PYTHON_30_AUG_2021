# Write names taken from user in sorted order into sorted_names.txt

f = open("sorted_names.txt", "wt")
names = []
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

for n in sorted(names):
    f.write(n + "\n")


f.close()
