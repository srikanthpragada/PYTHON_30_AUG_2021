
total = 0
for i in range(5):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    total += num
else:
    print("Done")



print(f"Total = {total}")