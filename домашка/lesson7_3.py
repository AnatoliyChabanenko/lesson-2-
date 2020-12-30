def make_operation (x,*args):
    s=0
    d=1
    for i in args:
        if x== '+':
            s+=i
            return s
        elif x== '-':
            s-=i
            return s
        else:
            d*=i
    return d
print(make_operation('*',5,5))