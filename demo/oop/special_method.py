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

    def __int__(self):
        return self.age

    def __add__(self, age):
        return Person(self.name, self.age + age)


p1 = Person("Abc", 20)
p2 = Person("Abc", 20)
p3 = Person("Abc", 22)

print(p1)  # p1.__str__()
print(p1 == p2)  # p1.__eq__(p2)
print(p1 == p3)
print(p3 < p2)  # p3.__gt__(p2)
print(int(p1))  # p1.__int__()

p4 = p1 + 10  # p1.__add__(10)
print(p4)
