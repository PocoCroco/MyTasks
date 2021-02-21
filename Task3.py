class CheckNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


numbers = []
while True:
    try:
        number = input('Введите число: ')
        if number == 'stop':
            break
        for el in number:
            if ord(el) > 57 or 46 < ord(el) < 48 or 44 < ord(el) < 46 or ord(el) < 44:
                raise CheckNumber('Вы ввели не число!')
    except CheckNumber as err:
        print(err)
    else:
        numbers.append(number)

print(numbers)



