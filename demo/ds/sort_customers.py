data = ["Tom,91911111", "Andy,484848444", "Larry,29291122",
        "Steve,33939333", "Larry,3929111112"]

customers = {}
for v in data:
    name, mobile = v.split(",")
    customers[name] = mobile

for name, mobile in sorted(customers.items()):
    print(f"{name:15} {mobile}")
