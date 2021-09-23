class Student:
    # Constructor
    def __init__(self, name, course, feepaid=0):
        # Object attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid

    # Methods
    def show(self):
        print(self.name, self.course, self.feepaid)

    def payment(self, amount):
        self.feepaid += amount

    def due_amount(self):
        if self.course == 'Python':
            return 5000 - self.feepaid
        else:
            return 10000 - self.feepaid


s1 = Student("Scott", "Python")  # Create object and call constructor
# print(s1.feepaid)
s1.show()  # invoke method
s1.payment(3000)
print(s1.due_amount())

s2 = Student("Jack", "Java", 4000)
s2.show()
