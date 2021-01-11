a=[1,2,3]
b=[4,5,6]

def vectorAdd(a,b):
     return [x+y for (x,y) in zip(a,b)]
print(vectorAdd(a,b))


def vectorDiff(a,b):
    for i in a:
        c = [x-y for x,y in zip(a,b)]
    return c


def vectorMultiply(a, b):
    return sum([x*y for (x,y) in zip(a,b)])
print(vectorMultiply(a,b))


def l2(a):
    c= sum(x**2 for x in a)
    d=c**(1/2)
    return d
print(l2(a))
print(l2(b))


def D(a,b):
    c=vectorDiff(a,b)
    d=l2(c)
    return d
print(D(a,b))


def cosineAngle(a,b):
    c=vectorMultiply(a,b)
    d=l2(a)*l2(b)
    f=c/d
    return f
print(cosineAngle(a,b))