def min():
    alist=[1,5,6,2,63,32]
    diff=[]
    q=0
    z=alist[0]-alist[1]
    if z>0:
        z=z
    elif z<0:
        z=-z
    for x in range(0,5):
        q= alist[x]-alist[x+1]
        if q>0:
            q=q
        elif q<0:
            q=-q

        if q<z:
            z=q
            diff=[alist[x],alist[x+1]]
    return(diff)
    
print(min())



def max():
    blist=[0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
    z=0
    maxNum = 0
    for i in blist:
        if blist[i]==blist[i+1]==1:
            z += 1
            if z> maxNum:
                maxNum=z

        else:
            z = 0
    return maxNum 
print(max())


def stringIntersection():
    a="abcd325"
    b="5tDEDc3"
    for i in a:
        for j in b:
            if i==j:
                stringIntersection= print (i and j)

stringIntersection()
