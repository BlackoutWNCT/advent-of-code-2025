## Challenge 1: Open the safe

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

    Direction = str("")
    Distance = int(0)
    startingPosReq = bool(True)
    Combination = list([])
    Open = bool(False)

    while Open == False:

        Direction = str(input('Input Direction to turn the dial (\"L\" for Left, \"R\" for Right, \"E\" to End): '))
        
        if Direction.upper() not in ["L", "R", "E"]:
            Direction = str(input('Input Direction to turn the dial (\"L\" for Left, \"R\" for Right, \"E\" to End): '))

        if Direction in ["L", "R"]:

            Distance = int(input('Input number of clicks to turn the dial: '))

            if Distance not in range(0,99):
                Distance = int(input('Input number of clicks to turn the dial: '))

            if startingPosReq == True:
                startingPos = int(input('Input the starting position (Usually this is 0): '))
                startingPosReq = False
                currentPos = startingPos

            while Distance != 0:
                if Direction == "L":
                    currentPos = moveForward(currentPos)
                elif Direction == "R":
                    currentPos = moveBackward(currentPos)
                print("You turn the dial to " + str(currentPos))
                Distance -= 1

            Combination.append(currentPos)
        
        elif Direction == "E":
            Open = True

    print('Huzzar! The combination to the safe is ' + str(Combination))