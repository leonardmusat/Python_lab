class Account:
    def __init__(self, id, money_amount):
        self.id = id
        self.money_amount = money_amount


class SavingsAccount(Account):
    def __init__(self, id, money_amount):
        Account.__init__(self, id, money_amount)

    def deposit(self, new):
        self.money_amount = self.money_amount + new

    def withdrow(self, amount):
        if amount > self.money_amount:
            print("not sufficient money")
        else:
            self.money_amount = self.money_amount - amount


class CheckingAccount(Account):
    def __init__(self, id, money_amount):
        Account.__init__(self, id, money_amount)

    def interest_calculation(self, interest_rate, periods):
        return self.money_amount * interest_rate * periods


id = 1
money_amount = 3000
savings = SavingsAccount(id, money_amount)
savings.deposit(500)
checking = CheckingAccount(id, money_amount)
print("My parents sant 500 lei: ", savings.money_amount)
savings.withdrow(1000)
print("I need 1000 lei to pay my exams: ", savings.money_amount)
print()
print(checking.interest_calculation(0.04, 5))

