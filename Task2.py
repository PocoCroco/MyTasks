with open('f_task_2.txt', 'r') as f:
    content = f.readlines()
    print(content)
    print('Кол-во строк: ', len(content))
    for el in range(len(content)):
        string = content[el].split()
        print(f'Кол-во слов в строке {el+1}: {len(string)}')
