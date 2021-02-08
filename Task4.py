
with open('f_task_4.txt', 'r', encoding='UTF-8') as f:
    content = f.readlines()
    new_content = []
    for line in content:
        line = line.split()
        if line[0] == 'One':
            line[0] = 'Один'
        if line[0] == 'Two':
            line[0] = 'Два'
        if line[0] == 'Three':
            line[0] = 'Три'
        if line[0] == 'Four':
            line[0] = 'Четыре'
        line = ' '.join(line)
        print(line)
        new_content.append(line + '\n')
    print(new_content)

with open('f_task_4.1.txt', 'w', encoding='UTF-8') as f_2:
    f_2.writelines(new_content)
