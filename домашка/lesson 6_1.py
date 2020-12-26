#первая
v= [1 , 2, 3, 4,5,1 ,3 ,5, 7 ,7]
k=[]
for i in range (len(v)):
    k.append(i)
dicor = dict(zip(v, k))
print(dicor)
# вторая
#2
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
x=input('какой фрукт вас интересует:')
print (stock.get(x)*prices.get(x))

# последняя
d = {a: a ** 2 for a in range(1,11)}
print(d)