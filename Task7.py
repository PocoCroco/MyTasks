import json

with open('f_task_7.txt', 'r', encoding='UTF-8') as f:
    content = f.readlines()
    profits = []
    names = []
    only_profit = 0
    i = 0
    for line in content:
        i += 1
        line = line.split()
        profit = int(line[2]) - int(line[3])
        profits.append(abs(profit))
        names.append(line[0])
        if profit > 0:
            only_profit += profit
    average = only_profit // i

total = [
    {
        names[0]: profits[0],
        names[1]: profits[1],
        names[2]: profits[2],
        names[3]: profits[3],
    },
    {
        'average_profit': average
    }
]

with open('f_task_7.1.json', 'w') as json_f:
    json.dump(total, json_f)