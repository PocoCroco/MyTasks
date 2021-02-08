
with open('f_task_1.txt', 'w', encoding='UTF-8') as f:
    while True:
        a = f.write(input('Введите название продукта: '))
        f.write('\n')
        if not a:
            break
