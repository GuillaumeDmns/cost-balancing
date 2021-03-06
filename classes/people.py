class People:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._expenses = []
        self._refunds = []

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if len(new_name.strip()) > 0 and not new_name.isspace():
            self._name = new_name

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

    def plus_balance(self, amount):
        self._balance += amount

    def minus_balance(self, amount):
        self._balance -= amount

    def get_expenses(self):
        return self._expenses

    def add_expense(self, expense):
        self._expenses.append(expense)
        self.plus_balance(expense.get_amount())

    def add_refund(self, refund):
        self._refunds.append(refund)
