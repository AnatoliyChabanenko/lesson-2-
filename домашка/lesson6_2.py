#первая
v= [1 , 2, 3, 4,5,1 ,3 ,5, 7 ,7]
k=[]
for i in range (len(v)):
    k.append(i)
dicor = dict(zip(v, k))
print(dicor)
# последняя
d = {a: a ** 2 for a in range(1,11)}
print(d)