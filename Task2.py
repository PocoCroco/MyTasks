from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def f_expenses(self):
        pass


class Tuxedo(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 1:
            self.__size = 1
        elif h > 60:
            self.__h = 60
        else:
            self.__h = h

    def f_expenses(self):
        return 2*self.__h + 0.3


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 7:
            self.__v = 7
        elif v > 40:
            self.__v = 40
        else:
            self.__v = v

    def f_expenses(self):
        return self.__v/6.5 + 0.5


a = Tuxedo(int(input('Введите высоту костюма: ')))
b = Coat(int(input('Введите размер пальто: ')))
print(a.f_expenses())
print(b.f_expenses())
