class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует на полях тетради')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует домик')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует график роста акций')


a = Stationery(None)
b = Pen('pen')
c = Pencil('pencil')
d = Handle('handle')

a.draw()
b.draw()
c.draw()
d.draw()