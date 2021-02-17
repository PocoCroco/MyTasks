class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        w_p_sq = 25
        thickness = 5
        return self._length * self._width * w_p_sq * thickness / 1000


r = Road(float(input('Введите длину: ')), float(input('Введите ширину: ')))
print(r.mass(), 'т.')
print()
