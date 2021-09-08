st1 = "Abcdefde"
st2 = "dexyzd"

chars = []
for c in st1:
    if c not in chars and c in st2:
        print(c)
        chars.append(c)
