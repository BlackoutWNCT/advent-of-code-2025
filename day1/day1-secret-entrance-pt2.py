## Challenge 1: Open the Entrance

rotationKey = open("./rotations.txt")
keyList = []
for each in rotationKey:
    keyList.append(each)
rotationKey.close()

def moveForward(currentPos):
    if currentPos == 99:
        nextPos = 0
    else:
        nextPos = currentPos + 1
    return nextPos

def moveBackward(currentPos):
    if currentPos == 0:
        nextPos = 99
    else:
        nextPos = currentPos - 1
    return nextPos

if __name__ == '__main__':

    startingPos = int(50)
    currentPos = startingPos
    touchPoints = list([])
    
    for each in keyList:

        direction = str(each[0])
        distance = int(each[1:])

        while distance != 0:
            if direction == "L":
                currentPos = moveForward(currentPos)
            elif direction == "R":
                currentPos = moveBackward(currentPos)
            print("You turn the dial to " + str(currentPos))
            distance -= 1
            touchPoints.append(currentPos)

    zeroCount = touchPoints.count(0)
    print("The number of times the integer \'0\' is touched is " + str(zeroCount))