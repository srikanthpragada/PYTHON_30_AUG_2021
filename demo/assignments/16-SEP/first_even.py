def first_even(*nums):
    for n in nums:
        if n % 2 == 0:
            return n

    return None


n = first_even(5, 7, 10, 20)
print(n)
n = first_even(5, 7, 3)
print(n)

