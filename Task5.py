from functools import reduce


def sum_func(prev_el, el):
    return int(prev_el) + int(el)


with open('f_task_5.txt', 'w') as f:
    f.write('425 14 523 45 34 435 146 2987 14 634')

with open('f_task_5.txt', 'r') as f:
    content = f.read()
    content = content.split()
    print(content)
    print(reduce(sum_func, content))
