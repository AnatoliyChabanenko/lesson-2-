stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
mydict_k = dict.keys(stock)
print(dict.keys(stock))
x=input('какой фрукт вас интересует:')
try:
    if x not in mydict_k :
        pass
    print(stock.get(x) * prices.get(x))
except TypeError:
    print(f'может здесь какая-то шибка:\t' +x+'\t?')
