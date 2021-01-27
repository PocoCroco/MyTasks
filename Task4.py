some_phrase = input('Перечислите ваши любимые блюда через пробел: ')
some_phrase = some_phrase.split()
for ind, word in enumerate(some_phrase):
    if len(word) > 10:
        word = word[:10]
    print(ind + 1, word)
