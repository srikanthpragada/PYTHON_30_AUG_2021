def isvalidemail(email):
    return '@' in email and len(email) >= 3


f = open("emails.txt", "rt")  # filename, mode

emails = set()
for line in f.readlines():
    mails = line.strip().split(",")
    for v in filter(isvalidemail, mails):
        emails.add(v.strip())

f.close()

for e in sorted(emails):
    print(e)
