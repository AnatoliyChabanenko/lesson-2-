def make_country(x,y):
    return {'country': x, 'capital': y}

a = make_country('ukr','kiev')
print(a)
def prin_country (a):
    print(a.values())
prin_country(a)