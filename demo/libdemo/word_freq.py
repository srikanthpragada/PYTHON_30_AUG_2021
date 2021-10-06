import re

with open(r"c:\classroom\aug30\old_man.txt", "rt") as f:
    contents = f.read()

words = re.findall("\w+", contents)
word_freq = {}

for w in set(words):
    word_freq[w] = words.count(w)

for word, count in sorted(word_freq.items()):
    print(f"{word:20} {count:3}")
