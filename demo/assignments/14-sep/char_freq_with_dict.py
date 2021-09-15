st = "How do you do"

chars = {}

for c in set(st):
    chars[c] = st.count(c)

for ch, count in sorted(chars.items()):
    print(f"{ch} {count:2}")
