class DivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


divisible = int(input("Введите делимое: "))
divider = int(input("Введите делитель: "))

try:
    if divider == 0:
        raise DivisionError("Ошибка деления на ноль!")
    quotient = divisible / divider
except DivisionError as err:
    print(err)
else:
    print(f"Частное: {quotient}")