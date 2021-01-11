def EstPopSize(t1,c,t2):
    return (t1*c)/(t2)
print( EstPopSize(20,10,2))
print( EstPopSize(10,15,4))
print( EstPopSize(15,15,1))
'''
LifeData=[10, 8, 1]
for x[2] in LifeData:
    print((10*8)/(1)) 
'''

LifeData = [["Bison", 20, 10, 2], ["Wolf", 10, 15, 4], ["Praire Dog", 15, 15, 1], ["Mountain Lion", 10, 8,1]]
for d in LifeData:
   print(d[0] + " estimated population size = " + str(EstPopSize(d[1],d[2],d[3])))