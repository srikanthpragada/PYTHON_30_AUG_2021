# Print file contents

with open("names.txt", "rt") as f:
    for n in f.readlines():
        print(n.strip())
