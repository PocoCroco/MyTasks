user_s = int(input('Введите время в секундах: '))
h = user_s // 3600
m = (user_s - h * 3600) // 60
s = user_s - h * 3600 - m * 60

if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
if s < 10:
    s = '0' + str(s)

print(f'Время: {h}:{m}:{s}')
