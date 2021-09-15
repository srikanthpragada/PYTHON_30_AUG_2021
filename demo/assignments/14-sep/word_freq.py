st = "how do you do today how did you do yesterday"

words = st.split(" ")
for w in set(words):
   print(f"{w:10} {words.count(w):2}")
