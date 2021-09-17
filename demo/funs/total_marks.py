marks = "90,70,60,50,44,55"

total = 0
for n in marks.split(","):
    total += int(n)

print(total)

total = sum(map(int, marks.split(",")))
print(total)
