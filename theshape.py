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
print(calculateNewPositions([0,0]))