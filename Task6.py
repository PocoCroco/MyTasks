def int_func(string):
    new_string = ''
    for i in range(len(string)):
        if i == 0:
            new_string += chr(ord(string[i]) - 32)
        else:
            new_string += string[i]
    return new_string


some_word = 'constitution'
print(int_func(some_word))
