i = int(input('Введите кол-во наименований: '))
goods = []
name = []
price = []
quantity = []
unit = []

for el in range(i):
    name.append(input(f'Введите название товара {el+1}: '))
    price.append(input(f'Введите цену товара {el+1}: '))
    quantity.append(input(f'Введите кол-во товара {el+1}: '))
    unit.append(input(f'Введите ед. изм. товара {el+1}: '))
    goods.append((el + 1, {'название': name[el],
                           'цена': price[el],
                           'количество': quantity[el],
                           'ед': unit[el]}))

for el in goods:
    print(el[0], el[1])

unit = list(set(unit))

new_goods = {
    'название': name,
    'цена': price,
    'количество': quantity,
    'ед': unit
}

print('\n', new_goods)

