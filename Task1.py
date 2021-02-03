from sys import argv


def salary_func(a, h, p):
    return int(a)*int(h) + int(p)


name_script, wage, time, bonus = argv
print('Зарплата сотрудника: ', salary_func(wage, time, bonus))
