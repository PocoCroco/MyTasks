some_number = int(input('Введите число: '))
my_list = [10, 7, 7, 6, 4, 3, 3]
for number in range(len(my_list)):
    if some_number > my_list[number]:
        my_list.insert(number, some_number)
        break
    elif number == len(my_list) - 1:
        my_list.append(some_number)
print(my_list)