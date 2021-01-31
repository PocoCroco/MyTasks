def my_func(n_1, n_2, n_3):
    result = n_1 + n_2 + n_3 - min(n_1, n_2, n_3)
    return result
sum = my_func(int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')))
print(sum)
