f = open("emails.txt", "rt")  # filename, mode

emails = set()
for line in f.readlines():
    mails = line.strip().split(",")
    emails = emails.union(set(mails))

f.close()

for e in sorted(emails):
    print(e)
