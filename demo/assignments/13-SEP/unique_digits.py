nums = [123, 434, 5554, 567]

digits = set()  # Empty set

for n in nums:
    for c in str(n):
        digits.add(c)

print(sorted(digits))

