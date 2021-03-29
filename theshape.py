positions=[[0,1,"alive"],[1,0,"alive"],[-1,0,"alive"],[0,-1,"alive"]]
newpositions=[]
turns = 1
#detectCollision(position)
def detectCollision(position,checkList):
    for i in range(len(checkList)):
        if position[0] == checkList[i][0] and position[1] == checkList[i][1]:
            checkList[i][2] = "dead"
            return [True,checkList]
    return [False,checkList]
#TODO: growTheShapeNTimes(n)
#TODO: countInTheNewPositions()
#calculateTheDiagonals(n)
def calculateTheDiagonals(n):
    x0 = 1
    x = range(n)
    for n1 in x:
        if n1 % 2 == 0:
            #do nothing
            u=1
        else:
            x0+=1
    return x0
def calculateTheHorizontals(n):
    x0 = 0
    x = range(n)
    for n1 in x:
        if n1 % 2 == 0:
            x0 += 2
    return x0
#TODO: calculateNewPositions()
def calculateNewPositions(position):
    isSideWays = False
    if turns % 2 == 0:
        isSideWays = True
    newposes = [[0,0,"alive"],[0,0,"alive"]]
    #TODO: actually calculate the new positions
    return newposes
#emptyTheNewPositions()
def emptyTheNewPositions():
    newpositions.clear()
def areaOfAnOctagon(n):
    a1 = (n*calculateTheDiagonals(n))/2
    a2 = (n*calculateTheHorizontals(n))/2
    return 4*a1+4*a2
def printStuff(y):
    x = range(y)
    for n in x:
        print(calculateTheHorizontals(n),calculateTheDiagonals(n),4*calculateTheDiagonals(n),4*calculateTheHorizontals(n))
print(areaOfAnOctagon(9000000))