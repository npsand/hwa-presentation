
from cmath import sqrt
from random import randint

arr = [[0,0,0], [0,0,0], [0,0,0], [0,0,0] ,[0,0,0] ,[0,0,0]]

#Calculates the distance between first and last cordinates in cordinate array
def getDistance():
    dx = arr[5][0]-arr[0][0]
    dy = arr[5][1]-arr[0][1]
    dz = arr[5][2]-arr[0][2]
    d = sqrt(((dx)**2 + (dy)**2 + (dz)**2))
    print("Distance between first and 5th frame: ", d)
    print(" ")
 
#Moves every item in the list by one ans add new cordinates (x, y, z) to the beginning of the list.
def addToQueue(x, y, z):
    for q in range(1,6):
        arr.insert(6-q, arr.pop(5-q))

    arr[0][0] = x
    arr[0][1] = y
    arr[0][2] = z

    getDistance()

#Genereates random cordinates to be added to the list.
for i in range(10):
    x = randint(-10, 10)
    y = randint(-10, 10)
    z = randint(-10, 10)

    addToQueue(x, y, z)




