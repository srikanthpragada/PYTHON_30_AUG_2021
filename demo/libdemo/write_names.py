names = ['Larry', 'Mark', 'Sergy', 'Louis', 'Jeff']

f = open("names.txt", "wt")  # filename, mode

for n in names:
    f.write(n + "\n")

f.close()
