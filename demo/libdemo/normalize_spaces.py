import re

with open(r"c:\classroom\aug30\old_man_v2.txt", "rt") as f:
    contents = f.read()

new_contents = re.sub(" +", ' ', contents)
new_contents = re.sub("\n+", '\n', new_contents)

with open(r"c:\classroom\aug30\old_man_v2.txt", "wt") as f:
    f.write(new_contents)
