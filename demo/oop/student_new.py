class Student:
    courses = {"Python": 5000, "Java": 10000, "DS": 15000}

    # Constructor
    def __init__(self, name, course, feepaid=0):
        if course not in Student.courses:
            raise ValueError("Invalid Course!")

        self.name = name
        self.course = course
        self.feepaid = feepaid

    # Methods
    def __str__(self):
        return f"{self.name} - {self.course} - {self.feepaid}"

    def payment(self, amount):
        self.feepaid += amount

    def total_fee(self):
        return Student.courses[self.course]

    def due_amount(self):
        return self.total_fee() - self.feepaid


s1 = Student("Scott", "DS")  # Create object and call constructor
# print(s1.feepaid)
print(s1)
s1.payment(3000)
print(s1.due_amount())

s2 = Student("Jack", "Java", 4000)
print(s2)  # s2.__str__()
