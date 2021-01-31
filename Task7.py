def int_func(string):
    new_string = ''
    string = string.split(' ')
    for el in range(len(string)):
        for i in range(len(string[el])):
            if i == 0:
                new_string += chr(ord(string[el][i]) - 32)
            else:
                new_string += string[el][i]
        if el + 1 != len(string):
            new_string += ' '
    return new_string

some_phrase = "hey it's michael here"
print(int_func(some_phrase))