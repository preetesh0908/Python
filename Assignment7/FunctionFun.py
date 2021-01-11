#Problem 1:
x = [[1,2],[[3,4],5,[6]],7]
y = [["a",["b",["c","d","e"]],["f","g",["h","i","j"]],"k"],"l"]
z = [[0,1], "small", [[5, 23], "car"]]
w = [1]
def flatten(x): return flatten(x[0]) + (flatten(x[1:]) if len(x) > 1 else []) if type(x) is list else [x] 
print(flatten(x))
print(flatten(y))
print(flatten(z))
print(flatten(w))
print("\n")

#Problem 2:
c= "regular"
b="hablar"
def conjugate(c):
    d= "ar"
    a=["Yo", "Tu", "El", "Nosotros", "Vosotros", "Ustedes"]
    e=["o","as","a","amos", "ais", "an"]
    newwordlist=[]
    for i,j in zip(a,e):
        newword=i+" "+ c[:-2]+j
        newwordlist.append(newword)
    return newwordlist
for i in conjugate(c):
    print(i)
print("\n")
for j in conjugate(b):
    print(j)
print("\n") 
       
#Problem 3:
def matImp(A,B):
    if A==0 and B==1:
        return 1
    elif A==0 and B==0:
        return 1
    elif A==1 and B==0:
        return 0
    elif A==1 and B==1:
        return 1
print(matImp(1,0))
print("\n")

#Problem 4:

a=open("C:\\python\\magic.txt", mode='r')
b=[]
def sortNumbers(a): 
    for i in a:
        b.append(i[:-1])
    for j in range(len(b)):
        for k in range(len(b)-1):
            if (b[k] > b[k+1]):
                b[k], b[k+1] = b[k+1],b[k]
    return b

print(sortNumbers(a))
q=open("C:\\python\\malamute.txt", 'w')
a.close()
for g in b:
        q.write(g+"\n")
q.close()
print("\n")

#Problem 5:
class Book:
    def __init__(self, title, firstName, lastName, price, quantity):
        self.title = title
        self.firstName = firstName
        self.lastName= lastName
        self.price= price
        self.quantity= quantity

    def getprice(self):
        return self.price

    def inStock(self):
        if self.quantity > 0:
            return True
        else:
            return False

    def sold(self):
        if self.quantity > 0:
            self.quantity = self.quantity - 1
        else:
            print("Out of Stock")

    def available(self):
        return self.quantity

        
bookList = []
bookList.append(Book("Brave New World", "Aldous", "Huxley", 12.75, 2))
bookList.append(Book("Jane Eyre", "Charlotte" , "Bronte", 10.50, 4))
bookList.append(Book("Pride and Prejudice", "Jane" , "Austin", 15.00, 1))
bookList.append(Book("In Search of Lost Time", "Marcel" , "Proust", 9.00, 0))
bookList.append(Book("Wuthering Heights", "Emily" , "Bronte", 10.50, 3))
bookList.append(Book("Rebecca", "Daphne" , "du Maurier", 9.00, 2))

def findBook(title):
    for i in bookList:
        if i.title == title:
            return i

wh = "Wuthering Heights"
whBook = findBook(wh)
print("{0} sells for {1}".format(wh, whBook.getprice()))

isolt = "In Search of Lost Time"
isoltBook = findBook(isolt)
isoltBook.sold()

bnw = "Brave New World"
bnwBook = findBook(bnw)
print("{0}: {1} copies available".format(bnw, bnwBook.available()))
bnwBook.sold()
print("{0}: {1} copies available".format(bnw, bnwBook.available()))
