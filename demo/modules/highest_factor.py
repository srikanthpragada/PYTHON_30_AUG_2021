import sys

for n in sys.argv[1:]:
    num = int(n)
    for i in range(num // 2, 0, -1):
        if num % i == 0:
            print(f"{num:5} {i:5}")
            break
