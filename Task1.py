import time


class TrafficLight:
    __color = 'red'

    def running(self, color):
        if self.__color != color:
            print('Ошибка')
            return True
        self.__color = color
        if color == 'red':
            print('Красный')
            time.sleep(7)
            print('Жёлтый')
            self.__color = 'yellow'
        elif color == 'yellow':
            print('Жёлтый')
            time.sleep(2)
            print('Зелёный')
            self.__color = 'green'
        elif color == 'green':
            print('Зелёный')
            time.sleep(5)
            print('Красный')
            self.__color = 'red'
        else:
            return True


tl = TrafficLight()
while True:
    a = tl.running(input('Цвет: '))
    if a:
        break
