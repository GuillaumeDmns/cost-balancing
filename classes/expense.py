class Expense:
    def __init__(self, name, amount):
        self._name = name
        self._amount = amount

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_amount(self):
        return self._amount

    def set_amount(self, new_amount):
        self._name = new_amount
