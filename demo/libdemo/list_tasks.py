from datetime import *

f = open("tasks.txt", "rt")
ef = open("errors.txt", "wt")

for line in f:
    parts = line.strip().split(",")
    if len(parts) == 3:
        try:
            sd = datetime.strptime(parts[1], "%d-%m-%Y")
            ed = datetime.strptime(parts[2], "%d-%m-%Y")
            days = (ed - sd).days
            print(f"{parts[0]:50} - {days} day(s)")
        except:
            ef.write(line)
    else:
        print(f"{parts[0]:50} - ongoing")

f.close()
ef.close()
