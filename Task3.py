from functools import reduce


def sum_func(prev_el, el):
    return float(prev_el) + float(el)

with open('f_task_3.txt', 'r', encoding='UTF-8') as f:
    i = 0
    salaries = []
    for emp in f:
        i += 1
        string = emp.split()
        salaries.append(string[1])
        if float(string[1]) < 20000:
            print(emp, end='')
    average = round(reduce(sum_func, salaries) / i, 2)
    print('\nСредняя зарплата сотрудников:', average)
