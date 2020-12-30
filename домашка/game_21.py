import random

koloda = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'valet': 2,
    'dama': 3,
    'korol': 4,
    'tuz': 11,

}


def igra(koloda):
    karta = koloda.popitem()
    znachenie = karta[1]
    kakayakarta = karta[0]
    return znachenie
print(igra(koloda))
i = igra(koloda)
while i <= 21:
    input('введи что-то:')
    i += igra(koloda)
    print(i)
