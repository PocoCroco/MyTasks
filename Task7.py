class ComplexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


a = ComplexNumber(20 + 3j)
b = ComplexNumber(24 + 5j)
print(a + b)
print(a * b)