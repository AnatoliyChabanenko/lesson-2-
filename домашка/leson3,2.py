a = input('Введите номер телефона  : ')
b = len(a)

try:
   opa = int(a)
except ValueError:
   print("That's not an int!")
if b == 10:
    print('вы правельно увели номер, поздравляю')
if b < 10:
    print('маловато цыфр в вашем номере')
if b > 10:
    print ('что-то много цыфр')