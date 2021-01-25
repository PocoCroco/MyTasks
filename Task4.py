number = input('Введите целое положительное число: ')
i = 1
max = number[0]
while i < len(number):
    if number[i] > max:
        max = number[i]
    i += 1
print("Самая большая цифра =", max)


