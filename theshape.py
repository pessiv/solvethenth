positions=[[1,1,"alive"],[1,0,"alive"],[-1,0,"alive"],[0,-1,"alive"]]
newpositions=[]
turn = 1

#detectCollision(position)
def detectCollision(position):
    for i in range(len(positions)):
        if position[0] == positions[i][0] and position[1] == positions[i][1]:
            positions[i][2] = "dead"
            return True
    return False
#TODO: growTheShapeNTimes(n)
#TODO: countInTheNewPositions()
#TODO: emptyTheNewPositions()
