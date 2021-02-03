def fact(n):
    number = 1
    for i in range(1, n + 1):
        number = number * i
        yield number


for el in fact(10):
    print(el)
