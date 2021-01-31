def division(number_1, number_2):
    try:
        result = number_1 / number_2
        return result
    except ZeroDivisionError as e:
        print(e)

print(division(int(input('Введите первое число: ')), int(input('Введите второе число: '))))