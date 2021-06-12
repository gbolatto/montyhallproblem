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

    stage1 = Stage()
    
    stage1.randomizeDoors()

    print("A car is behind one door. Goats are behind the others.")
    print("[0, 1, 2]")
    print("Choose a door: ")
    doorChoiceRaw = input()

    doorChoice = int(doorChoiceRaw)

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
    doorChoice2Raw = input()

    doorChoice2 = int(doorChoice2Raw)

    if stage1.doors[int(doorChoice2)] == "car":
        print("You win a car!")

    if stage1.doors[int(doorChoice2)] == "goat":
        print("You lose!")

