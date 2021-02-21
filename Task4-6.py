class ValidatorError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    goods = []

    @classmethod
    def get_the_appliance(cls, appliance, battery, price, energy,
                          ink_param=None, img_q_param=None, size_param=None):
        product = dict()
        product["Наименование"] = appliance
        product["Батарея"] = battery
        product["Цена"] = price
        product["Расход энергии"] = energy
        if ink_param:
            product["Расход чернил"] = ink_param
        elif img_q_param:
            product["Качество изображения"] = img_q_param
        elif size_param:
            product["Размер оборудования"] = size_param
        Warehouse.goods.append(product)


class OfficeSupplies:
    def __init__(self, battery, price, energy):
        try:
            self.battery = battery
            self.price = price
            self.energy = energy
            for el in self.battery, self.price, self.energy:
                for sym in el:
                    if ord(sym) > 57 or 46 < ord(sym) < 48 or 44 < ord(sym) < 46 or ord(sym) < 44:
                        raise ValidatorError('Вы ввели не число!')
        except ValidatorError as err:
            print(err)
            self.battery = input('Введите объём батареи: ')
            self.price = input('Введите цену товара: ')
            self.energy = input('Введите расход энергии: ')


class Printer(OfficeSupplies):
    def __init__(self, battery, price, energy, ink):
        super().__init__(battery, price, energy)
        Warehouse.get_the_appliance(Printer.__name__, battery, price, energy, ink_param=ink)


class Scanner(OfficeSupplies):
    def __init__(self, battery, price, energy, img_quality):
        super().__init__(battery, price, energy)
        Warehouse.get_the_appliance(Scanner.__name__, battery, price, energy, img_q_param=img_quality)


class Xerox(OfficeSupplies):
    def __init__(self, battery, price, energy, size):
        super().__init__(battery, price, energy)
        Warehouse.get_the_appliance(Xerox.__name__, battery, price, energy, size_param=size)


while True:
    name_user = input('Введите наименование товара: ')
    battery_user = input('Введите объём батареи: ')
    price_user = input('Введите цену товара: ')
    energy_user = input('Введите расход энергии: ')
    add_param = input('Введите доп. парам: ')
    if name_user == 'printer':
        a = Printer(battery_user, price_user, energy_user, add_param)
    elif name_user == 'scanner':
        a = Scanner(battery_user, price_user, energy_user, add_param)
    elif name_user == 'xerox':
        a = Xerox(battery_user, price_user, energy_user, add_param)
    else:
        break

print(Warehouse.goods)
