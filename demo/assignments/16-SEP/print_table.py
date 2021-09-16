def table(num, length=10):
    for i in range(1, length + 1):
        print(f"{num:3}  * {i:2} = {i * num :5}")


table(15, 5)
table(23)