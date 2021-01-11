import random
def bubbleSort(xlst):
    for i in range(len(xlst)):
        for j in range(len(xlst) - 1):
            if (xlst[j] > xlst[j+1]):
                xlst[j], xlst[j+1] = xlst[j+1],xlst[j]
             
size = int(input("Enter the number of random numbers to generate: "))

alist = []
for i in range(size):


 # append adds an element to a list
 alist.append(random.randrange(50))

print(alist)
bubbleSort(alist)
print(alist)



def rockSort(xlst):
    for i in range(len(xlst)):
        for j in range(len(xlst) - 1):
            if (xlst[j] < xlst[j+1]):
                xlst[j], xlst[j+1] = xlst[j+1],xlst[j]
             
size = int(input("Enter the number of random numbers to generate: "))

alist = []
for i in range(size):


 # append adds an element to a list
 alist.append(random.randrange(50))

print(alist)
rockSort(alist)
print(alist)


'''
#The random.randrange(50)) gives us random numbers that are in the indext of 50 i.e, numbers from 0 to 49 (0,1,2,3....48,49)

'''