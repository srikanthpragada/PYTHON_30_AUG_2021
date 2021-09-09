nums = []

for i in range(5):
    n = int(input("Enter a number :"))
    if n not in nums:
        nums.append(n)

for n in nums:
    print(n)
