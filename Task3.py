class Cell:
    def __init__(self, whole_q, q_a_row):
        self.scheme = ''
        self.whole_q = whole_q
        self.whole_q_order = whole_q
        self.q_a_row = q_a_row

    def __add__(self, other):
        return self.whole_q + other.whole_q

    def __sub__(self, other):
        if self.whole_q - other.whole_q < 0:
            return 'Ошибка вычисления'
        return self.whole_q - other.whole_q

    def __mul__(self, other):
        return self.whole_q * other.whole_q

    def __truediv__(self, other):
        return self.whole_q // other.whole_q

    def make_order(self):
        if self.whole_q_order % self.q_a_row != 0:
            rows = self.whole_q_order // self.q_a_row + 1
        else:
            rows = self.whole_q_order // self.q_a_row
        for i in range(rows):
            if self.whole_q_order > 0 + self.q_a_row:
                self.scheme += '*' * self.q_a_row
                self.scheme += '\n'
            else:
                self.scheme += '*' * abs(self.whole_q_order)
            self.whole_q_order -= self.q_a_row
        return self.scheme


a = Cell(13, 4)
b = Cell(25, 7)
print(a.make_order(), '\n')
print(b.make_order(), '\n')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
