import random

holeNum = 0
running = True
def welcome():
    print("Welcome to Virtual Disc Golf!\n")
def discSelect():
    print("1.) Driver (D)\n2.) Mid-Range (M)\n3.) Approach(A)\n4.) Putter (P)\n")
    disc = input("Please select a disc: ")
    return disc

# def holeCount(holeNum):
#     holeNum += 1
#     return holeNum

def holeDetail():
    holeLength = random.randrange(100, 300)
    print("Hole 1 is " + str(holeLength) + " feet long!")
    return holeLength

welcome()
holeDistance = holeDetail()
distanceRemaining = holeDistance

while running == True:
    disc = discSelect()

    if disc == "D":
        distanceGained = 150
        print("\nDriver selected!\n\nYou gained " + str(distanceGained) + " feet.\n")
        distanceRemaining = distanceRemaining - distanceGained
        if distanceGained == holeDistance:
            print("You aced!")
        elif distanceGained > distanceRemaining:
            distanceRemaining = abs(distanceRemaining)
        print(str(distanceRemaining) + " feet remaining\n")
    elif disc == "M":
        distanceGained = 80
        print("\nMidrange selected!\n\nYou gained " + str(distanceGained) + " feet.\n")
        distanceRemaining = distanceRemaining - distanceGained
        if distanceGained == holeDistance:
            print("You aced!")
        elif distanceGained > distanceRemaining:
            distanceRemaining = abs(distanceRemaining)
        print(str(distanceRemaining) + " feet remaining\n")
    elif disc == "A":
        distanceGained = 20
        print("\nApproach selected!\n\nYou gained " + str(distanceGained) + " feet.\n")
        distanceRemaining = distanceRemaining - distanceGained
        if distanceGained == holeDistance:
            print("You aced!")
        elif distanceGained > distanceRemaining:
            distanceRemaining = abs(distanceRemaining)
        print(str(distanceRemaining) + " feet remaining\n")
    elif disc == "P" and distanceRemaining <= 10:
        print("You successfully putted in from " + str(distanceRemaining) + " feet.")
        distanceRemaining = 0
    else:
        print("Disc not selected. No distance gained")
        distanceRemaining = holeDistance - distanceGained

    if distanceRemaining == 0:
        print("You completed this hole. Thanks for playing!")
        running = False