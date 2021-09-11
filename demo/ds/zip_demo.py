names = ['Larry', 'Steve', 'Mark', 'Scott']
ages = [45, 35, 50]

for idx, n in enumerate(names):
    print(f"{n:15}  {ages[idx]:2}")

for t in zip(names, ages):
    print(t)

for name, age in zip(names, ages):
    print(f"{name:15}  {age:2}")
