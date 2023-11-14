class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def say(self):
        pass

class Engineer(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)

    def say(self):
        string = "The product will be ready by the end of the month"
        return string

    def do(self):
        return "I build, adapt and crate."

    def __str__(self):
        return self.name


class Manager(Employee):
    def __init__(self, name, salary, team):
        Employee.__init__(self, name, salary)
        self.team = team

    def say(self):
        return "We will increase your salary by the end of the year"

    def get_team(self):
        rez = []
        for a in self.team:
            rez.append(str(a))
        return rez

class Salesperson(Employee):
    def __init__(self, name, salary, product_investment):
        Employee.__init__(self, name, salary)
        self.product_investment = product_investment

    def say(self):
        return "This product didn't failed any test"

    def sellprice(self):
        return self.product_investment + 0.1*self.product_investment

    def __str__(self):
        return self.name


e1 = Engineer("Ionel", 4000)
e2 = Engineer("Gheorghe", 4500)
s = Salesperson("Ioana", 4250, 10000)
list = [e1, e2, s]
m = Manager("Marius", 7000, list)
print(e1.name, ": ", e1.say())
print(e1.name, ": ", e1.do())
print(s.name, ": ", s.say())
print(s.name, ": We sell our produc with", s.sellprice())
print(m.name, ": ", m.say(), " My team is : ", m.get_team())