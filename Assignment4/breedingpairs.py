masbp=[(1990,5),(1991,6),(1992,7),(1993,9),(1994,9),
       (1995,9),(1996,10),(1997,9),(1998,9),(1999,11),
       (2000,12),(2001,12),(2002,12),(2003,15),(2004,),
       (2005,),(2006,25)] #Massachusetts 

 
def stateTotalBP(masbp):
    sum = 0
    for i in masbp:
        if len(i)==2:
            sum = sum +i[1]
    return sum
print(stateTotalBP(masbp))

def yearMax(x):
    foo=0
    maxYear=0
    for i in x:
        if len(i) == 2:
            if i[1]>foo:
                foo=i[1] 
                maxYear=i[0]      
    return maxYear    
print(yearMax(masbp))


def stateAvgBP(y):
    q=0
    for i in y:
        if len(i)==2:
            q=q+1
    return (stateTotalBP(masbp)/q)
print(stateAvgBP(masbp))