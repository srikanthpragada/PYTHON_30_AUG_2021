def ispass(n):
    return n >= 50


marks = ["90,45,66,77", "47,66,45,88", "33,33", "58,79,90"]

for m in marks:
    ml = map(int, m.split(","))   # Convert str to int
    # passed = list(filter(ispass, ml))  # Convert filter to list
    # print(len(passed))
    count = 0
    for v in ml:
        if v >= 50:
            count += 1

    print(count)
