class Employee(object):
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def changejob(self, job):
        self.job = job;

    def __str__(self):
        return f"{self.name} - {self.job}"


class Consultant(Employee):
    def __init__(self, name, job, rate, hours=0):
        super().__init__(name, job)
        self.rate = rate
        self.hours = hours

    def getsalary(self):
        return self.hours * self.rate

    # Overriding
    def __str__(self):
        return f"{super().__str__()} - {self.rate} - {self.hours}"


class SalariedEmployee(Employee):
    def __init__(self, name, job, salary):
        super().__init__(name, job)
        self.salary = salary

    def getsalary(self):
        return self.salary

    def __str__(self):
        return f"{super().__str__()} - {self.salary}"


c = Consultant("James", "DBA", rate=1000, hours=10)
c.changejob("Oracle DBA")
print(c)

print(isinstance(c, Consultant))
print(isinstance(c, Employee))
print(isinstance(10, int))
print(issubclass(Consultant, Employee))
print(issubclass(Consultant, str))
