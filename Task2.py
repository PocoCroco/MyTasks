i = int(input("Введите кол-во карт: "))
cards = []
for card in range(1, i+1):
    cards.insert(card, input(f'Введите название карты {card}: '))
print(cards)

for card in range(len(cards)):
    if card % 2 != 0:
        cards.insert(card - 1, cards[card])
        cards.pop(card + 1)
print(cards)