m = int(input('Введите название месяца от 1 до 12: '))

winter = 'a',
spring = 'b',
summer = 'c',
autumn = 'd'

if m in [12, 1, 2]:
    winter = m
elif m in [3, 4, 5]:
    spring = m
elif m in [6, 7, 8]:
    summer = m
elif m in [9, 10, 11]:
    autumn = m

seasons = {
    winter: 'зима',
    spring: 'весна',
    summer: 'лето',
    autumn: 'осень'
}

print(f'Месяц под номером {m}: {seasons.get(m)}')
