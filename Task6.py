from functools import reduce


def sum_func(prev_el, el):
    return int(prev_el) + int(el)


with open('f_task_6.txt', 'r', encoding='UTF-8') as f:
    content = f.readlines()
    works = []
    subjects = []
    for line in content:
        line = line.split()
        subjects.append(line.pop(0))
        if '—' in line:
            line.remove('—')
        works.append(reduce(sum_func, line))

total = {
    subjects[0]: works[0],
    subjects[1]: works[1],
    subjects[2]: works[2],
    subjects[3]: works[3]
}
print(total)
