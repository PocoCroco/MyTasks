revenue = int(input("Введите сумму выручки фирмы в $: "))
costs = int(input("Введите сумму издержек фирмы в $: "))
profit = None
loss = None

if revenue - costs >= 0:
    profit = revenue - costs
    print(f"Ваша прибыль составляет: {profit}$")
else:
    loss = costs - revenue
    print(f"Сумма ваших убытков составляет: {loss}$")

if profit:
    profitability = revenue / profit * 100
    profitability = round(profitability, 2)
    print(f"Рентабельность выручки: {profitability}%")
    staff = int(input("Введите кол-во сотрудников: "))
    profit_per_one = profit / staff
    profit_per_one = round(profit_per_one, 2)
    print(f"Прибыль в расчёте на одного сотрудника: {profit_per_one}$")
