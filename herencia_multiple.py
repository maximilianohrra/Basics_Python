class Person():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def description(self):
        print("name: ", self.name, "\nage: ", self.age, "\ncity: ", self.city)


class Employee (Person):
    def __init__(self, name, age, city, salary, seniority):
        super().__init__(name, age, city)

        self.salary = salary
        self.seniority = seniority

    def description(self):
        super().description()

        print("seniority: ", self.seniority, "\nsalary: ", self.salary)


LeonelMessi = Person("Leonel", 33, "Barcelona")
JohnDoe = Employee("Mark", 23, "Nüremberg", "2500€", "Semi-Senior")

LeonelMessi.description()
print("-")
JohnDoe.description()
