class Expense:
    def __init__(self, name, amount):
        self._name = name
        self._amount = amount

    def get_name(self):
        return self._name

    def set_name(self, newname):
        self._name = newname

    def get_amount(self):
        return self._amount

    def set_amount(self, newamount):
        self._name = newamount
