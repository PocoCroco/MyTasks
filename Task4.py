def my_func(x, y):
    result = x ** y
    return result


def my_func_2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= 1 / x
    return result


print(my_func(10, -2))
print(my_func_2(2, -4))
