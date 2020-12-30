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

def mix (koloda):
    l = list(koloda.items())
    random.shuffle(l)
    d = dict(l)
    return d# перемешал колоду
c=mix (koloda)
def karta(c):
    karta = c.popitem()
    return karta# взял карту
v=karta(c)
print(v)
def karta_znachenie(v):
    znachenie = v[1]
    return znachenie
r=karta_znachenie(v)
print(r)
def kakaya_karta(c):
    kakayakarta = v[0]
    return kakayakarta
i=0
while i <= 21:
    input('введи что-то:')
    i += r
    print(i)
