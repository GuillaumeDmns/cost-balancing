class People:
    def __init__(self, name):
        self._name = name
        self._balance = 0
        self._expenses = []
        self._refunds = []

    def get_name(self):
        return self._name

    def set_name(self, newname):
        self._name = newname

    def get_balance(self):
        return self._balance

    def set_balance(self, newbalance):
        self._balance = newbalance

    def add_expense(self, expense):
        self._expenses.append(expense)

    def add_refund(self, refund):
        self._refunds.append(refund)
