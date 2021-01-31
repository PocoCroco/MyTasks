def sum_func(new_numbers, new_sum, err):
    new_numbers = new_numbers.split()
    for i in range(len(new_numbers)):
        try:
            new_sum += int(new_numbers[i])
        except ValueError as e:
            print(e)
            err = 1
            print('Сумма чисел до ошибки: ')
            return new_sum, err
    return new_sum, err


sum = 0
error = 0
while True:
    question = input('Выполнить операцию? (y/n): ')
    if question == 'y':
        numbers = input('Введите числа через пробел: ')
        sum, error = sum_func(numbers, sum, error)
        print(sum)
        if error == 1:
            break
    elif question == 'n':
        break
