statePop2015 = [("North Carolina",10042802), ("Maine",1329328), 
                ("RhodeIsland",1056298), ("Montana",1032949), ("Delaware",945934), 
                ("South Dakota",858469), ("California",39144818),("Michigan",9922576), 
                ("New Jersey",8958013), ("Virginia",8382993), ("Texas", 27469114),
                ("Florida",20271272), ("New York",19795791), ("Illinois",12859995), 
                ("Pennsylvania",12802503),("Ohio",11613423), ("Georgia",10214860), 
                ("Louisiana",4670724),("Kentucky",4425092), ("Oregon",4028977), 
                ("Oklahoma",3911338),  ("Connecticut",3590886), ("Puerto Rico",3474182),
                ("Iowa",3123899), ("Utah",2995919), ("Mississippi",2992333),
                ("Arkansas",2978204), ("Kansas",2911641), ("Nevada",2890845),
                ("New Mexico",2085109),("Nebraska",1896190), ("West Virginia",1844128),
                ("Idaho",1654930), ("Hawaii",1431603), ("New Hampshire",1330608),
                ("North Dakota",756927), ("Alaska",738432), ("District of Columbia",672228),
                ("Washington",7170351), ("Arizona",6828065),  ("Massachusetts",6794422), 
                ("Indiana",6619680),("Tennessee",6600299),("Missouri",6083672),("Maryland",6006401), 
                ("Wisconsin",5771337),("Minnesota",5489594),("Colorado",5456574),("South Carolina",4896146),
                ("Alabama",4858979),("Vermont",626042),("Wyoming",586107)]
def popsort(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
                if (x[j][1] > x[j+1][1]):
                    x[j], x[j+1] = x[j+1],x[j]
    return x

print(statePop2015)
print(popsort(statePop2015))
def statePop():
    y=input("Enter the name of state to know its population:")
    for j in statePop2015:
        if y==j[0]:
            return (j[1],int((j[1]/324893002)*100))
print (statePop())

def rank(a,x):
    alist=popsort(x)
    return alist[len(alist-a)]