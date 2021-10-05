import os

startdir = r"c:\classroom\aug30\demo"  # raw string
allfiles = os.walk(startdir)

count = 0
for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            count += 1
            print(dirname + "\\" + f)

print(f"Count = {count}")