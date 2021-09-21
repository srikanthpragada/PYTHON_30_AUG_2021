# Prime number

import sys

if len(sys.argv) < 2:
    print("Usage : python prime.py  <number>")
    exit()

num = int(sys.argv[1])
prime = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        prime = False
        break

if prime:
    print("Prime Number")
else:
    print("Not a prime number")
