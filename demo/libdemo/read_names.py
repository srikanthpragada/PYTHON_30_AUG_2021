f = open("names.txt", "rt")  # filename, mode

for n in f.readlines():
    print(n.strip())

f.close()
