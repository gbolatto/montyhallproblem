import random

class Stage:

    def __init__(self):
        self.doors = [ "goat", "car", "goat" ]
    
    def randomizeDoors(self):
        random.shuffle(self.doors)

    def removeDoor(self, chosenDoor):
        if self.doors[int(chosenDoor)] == "car":
            tempList = []
            for i in range(len(self.doors)):
                tempList.append(i)
            tempList.pop(chosenDoor)
            if "x" not in self.doors:
                random.shuffle(tempList)
                self.doors[tempList[0]] = "x"
        for i in range(len(self.doors)):
            if i != int(chosenDoor):
                if self.doors[i] != "car":
                    if "x" not in self.doors:
                        self.doors[i] = "x"

if __name__ == "__main__":

    wonWithSticking = 0
    wonWithChanging = 0
    lostWithSticking = 0
    lostWithChanging = 0

    runs = input("How many runs? ")

    for i in range(0, int(runs)):
        stage1 = Stage()
        
        stage1.randomizeDoors()

        print("A car is behind one door. Goats are behind the others.")
        print("[0, 1, 2]")
        print("Choose a door: ")
        doorChoice = random.randint(0,2)
        print(doorChoice)

        stage1.removeDoor(doorChoice)

        closedDoors = []
        for i in stage1.doors:
            if i != "x":
                closedDoors.append(stage1.doors.index(i))

        openedDoor = stage1.doors.index("x")
        print("Door {door} was opened to reveal a goat.".format(door=openedDoor))
        print("You can stay with your original door or switch to another")
        print(closedDoors)
        print("Choose a door: ")
        random.shuffle(closedDoors)
        doorChoice2 = closedDoors[0]
        print(doorChoice2)

        if doorChoice == doorChoice2:
            stuckWithChoice = True
            print("Stuck with choice")
        if doorChoice != doorChoice2:
            stuckWithChoice = False

        if stage1.doors[int(doorChoice2)] == "car":
            print("You win a car!")
            if stuckWithChoice == True:
                wonWithSticking += 1
            if stuckWithChoice == False:
                wonWithChanging += 1
        if stage1.doors[int(doorChoice2)] == "goat":
            print("You lose!")
            if stuckWithChoice == True:
                lostWithSticking += 1
            if stuckWithChoice == False:
                lostWithChanging += 1
    print(" ")
    print("{wonStick} won with sticking.".format(wonStick=wonWithSticking))
    print("{wonChange} won with changing.".format(wonChange=wonWithChanging))
    print("{lostStick} lost with sticking.".format(lostStick=lostWithSticking))
    print("{lostChange} lost with changing.".format(lostChange=lostWithChanging))
    totalWon = wonWithSticking + wonWithChanging
    print("{totalWon} total won.".format(totalWon=totalWon))
    totalLost = lostWithSticking + lostWithChanging
    print("{totalLost} total lost.".format(totalLost=totalLost))
    totalGames = totalWon + totalLost
    print("{totalGames} total games played.".format(totalGames=totalGames))
