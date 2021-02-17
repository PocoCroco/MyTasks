class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина повернула направо')
        elif direction == 'left':
            print('Машина повернула налево')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Вы превышаете скорость')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


speed = int(input('Скорость автомобиля: '))
color = input('Цвет автомобиля: ')
name = input('Название автомобиля: ')
is_police = input('Это полицейская машина?: ')

t = TownCar(speed, color, name, is_police)
s = SportCar(speed, color, name, is_police)
w = WorkCar(speed, color, name, is_police)
p = PoliceCar(speed, color, name, is_police)

t.go()
s.stop()
w.turn('right')
p.turn('left')
s.show_speed()
w.show_speed()
t.show_speed()
