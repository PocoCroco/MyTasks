class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
        self.full_name = name + ' ' + surname
        self.total_income = self._income.get('wage') + self._income.get('bonus')
    def get_full_name(self):
        return self.full_name

    def get_total_income(self):
        return self.total_income


a = Position('Sergei', 'Ivanov', 'manager', {'wage': 50000, 'bonus': 20000})
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
