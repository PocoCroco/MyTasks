class Matrix:
    def __init__(self, *args):
        if len(args) > 1:
            self.numbers = args
        else:
            self.numbers = args[0]
        self.l_matrix = []
        self.new_numbers = args

    def __add__(self, other):
        for el in range(len(self.new_numbers)):
            for num in range(len(self.new_numbers[el])):
                self.new_numbers[el][num] = int(self.numbers[el][num]) + int(other.numbers[el][num])
        return Matrix(self.new_numbers)

    def __str__(self):
        for el in self.numbers:
            for i in range(len(el)):
                el = list(el)
                el[i] = str(el[i])
            el = ' '.join(el)
            self.l_matrix.append(el)
        self.l_matrix = '\n'.join(self.l_matrix)
        return f'{str(self.l_matrix)}'


a = Matrix([35, 23, 9, 4, 498], [95, 2, 49, 6, 13], [3, 333, 29, 59, 49])
b = Matrix([94, 839, 9, 20, 30], [1, 32, 56, 38, 499], [25, 93, 348, 695, 7])
print(a, '\n')
print(b, '\n')
print(a + b)
