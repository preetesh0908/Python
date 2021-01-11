import math
def y(d,r,t):
    return (d*math.exp(r*t))

print (y(1000,0.02,10)) 
 


def N(n0, m, t):
    return (n0*math.exp(m*t))

print (N(500,100,4))


def rate(age):
    if 6<= age <= 10:
        speed=2
    elif 10 <=age<= 15:
        speed=2.5
    elif 16 <= age<= 18:
        speed=3
    else:
        speed=4
    return speed

width=30
walk=6

def DWtime(width,speed):
    nowalk=(width/speed)-walk
       
    return nowalk

print(DWtime(30,rate(7)))
