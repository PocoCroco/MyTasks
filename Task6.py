from itertools import count
from itertools import cycle

for el in count(-20):
    if el > 30:
        break
    else:
        print(el)

c = 0
for el in cycle(['WHATS', 'UP']):
    if c > 25:
        break
    print(el)
    c += 1
