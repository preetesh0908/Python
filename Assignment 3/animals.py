human=28 
hummingbird=30 
dog=45 
cat=30 
ostrich=43
cheetah=70

def distance(speed1, speed2, time):
    return (speed1*time)-(speed2*time)
print(distance(hummingbird,human,2))
print(distance(dog,cat,2))
print(distance(cheetah,ostrich,2))

print("After 30secs, the distance between the fastest and the slowest creature is " + str(distance(cheetah, human, 30)))

print("After 1 minute, the distance between the slowest and the second slowest creature would be " + str(distance(hummingbird,human,1/60)))

speed=45/1760
distance=100
def vroom(speed, distance):
    time=distance/speed
    return time
print(str((vroom(45/1760,100))/60) + "seconds would be taken by a dog to travel 100 yards")