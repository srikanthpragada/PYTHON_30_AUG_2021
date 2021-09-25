class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age


people = [Person("A", 20), Person("B", 15), Person("C", 18)]
for p in sorted(people):
    print(p)

for p in sorted(people, key=lambda p: p.name):
    print(p)
