
st = "How do you do"

for c in sorted(set(st)):
    print(f"{c} {st.count(c)}")
