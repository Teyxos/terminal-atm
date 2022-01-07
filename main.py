class BankAccount:
    def __init__(self, initial_amount):
        try:
            with open("./logs.txt", "r") as file:
                content = file.read()
                content = content.split("amount:")
                self.amount = content[-1]
        except Exception:
            self.amount = initial_amount


user = BankAccount(30.00)
