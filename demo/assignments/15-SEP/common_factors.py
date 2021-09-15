def common_factors(n1, n2):
    small = n1 if n1 < n2 else n2
    for i in range(2, small // 2 + 1):
        if n1 % i == 0 and n2 % i == 0:
            print(i)


common_factors(10, 15)
common_factors(135, 255)



