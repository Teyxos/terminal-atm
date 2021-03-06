from datetime import datetime
from os import pardir


def trasaction(func):
    def wrapper(self, amount):
        with open("./logs.txt", "a") as logs:
            func(self, amount)
            logs.write(f"Start transaction:{datetime.now()}\t")
            logs.write(f"End transaction:{datetime.now()}\n")

    return wrapper


class BankAccount:
    def __init__(self, initial_amount):
        try:
            with open("./logs.txt", "r") as file:
                content = file.read()
                content = content.split("\t")
                content = content[-3]
                content = content.split("Amount:")
                self.amount = content[1]
        except Exception:
            self.amount = initial_amount

    @trasaction
    def deposit(self, amount):
        try:
            self.amount = float(self.amount)
        except ValueError:
            pass

        total = self.amount + amount

        with open("./logs.txt", "a") as logs:
            logs.write(f"Deposited:{amount}\t Amount:{total}\t")

        self.amount = total

    @trasaction
    def withdraw(self, amount):
        try:
            self.amount = float(self.amount)
        except ValueError:
            pass

        if self.amount < amount:
            print(f"You can't do that transaction!\t You have {self.amount} and you are trying to withdraw {amount}")
            exit(0)
        else:
            total = self.amount - amount

        with open("./logs.txt", "a") as logs:
            logs.write(f"Withdraw:{amount}\t Amount:{total}\t")

        self.amount = total

    def get_amount(self):
        with open("./logs.txt", "r") as logs:
            content = logs.read()
            content = content.split("\t")
            content = content[-3]
            content = content.split("Amount:")
            total = content[1]

        self.amount = total

        return total


# Create the Bank Account or accesing via logs.txt
user = BankAccount(0.00)

# Deposit
user.deposit(1000.00)

# Withdraw
user.withdraw(1000.00)

# Withdraw with less money
user.withdraw(1000.00)
