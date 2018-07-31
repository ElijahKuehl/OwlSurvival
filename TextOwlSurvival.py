from random import randint


class snowy_owl(object):
    def __init__(self):
        self.flying = False
        self.hiding = False
        self.target = False
        self.energy = 5
        self.score = 0

    # Makes the Owl Hide or Unhide, a good source of points, as you can Hide and Unhide for 1 Energy but 2 Points.
    def hide(self, name):
        if self.flying is False:
            if not self.hiding:
                print "\n", name, "hid deep into the snow."
                self.hiding = True
                self.energy -= 1
            elif self.hiding:
                print "\n", name, "came out of the snow."
                self.hiding = False
        else:
            print "\nYou are too high up to hide!"
            self.score -= 1

    # Makes the Owl Fly or Land, giving you an edge for Searching and Attacking.
    def fly(self, name):
        if not self.flying:
            print "\n", name, "flew up into the sky."
            self.flying = True
            self.energy -= 2
        elif self.flying:
            print "\n", name, "glided to the ground."
            self.flying = False

    # Makes the Owl search for food. The chance of finding something depends if you're Flying or not.
    def search(self, name):
        if self.flying:
            accuracy = 2
            print "\n", name, "looks onto the ground..."
        elif not self.flying:
            accuracy = 3
            print "\n", name, "looks across the ground..."
        else:
            accuracy = 1
        search = randint(1, accuracy)
        if search == 1:
            print name, "found a mouse! Go in for the Attack!"
            self.energy += 1
            self.target = True
        else:
            print name, "didn't find anything."
            self.target = False
        self.energy -= 1

    # Makes the Owl Attack if there's a target. The chance of catching it depends on your Flying and Hiding status.
    def attack(self, name):
        skill = 0
        if self.hiding:
            self.hiding = False
            print "\n", name, "came out of the snow."
            skill -= 1
        else:
            print
        if self.target:
            if self.flying:
                print name, "dives..."
                skill += 2
                chance = randint(1, skill)
                self.flying = False
            else:
                print name, "creeps up to the target..."
                skill += 3
                chance = randint(1, skill)
            if chance == 1:
                print name, "caught the mouse!"
                self.energy += 4
                self.target = False
            else:
                print name, "missed the mouse!"
                print "The mouse got away!"
                self.energy -= 1
                self.target = False
        else:
            print "There is nothing to attack!"
            self.score -= 1

    # Brings up the menu with all the actions to preform.
    def start(self, name):

        print "What would you like", name, "to do?"
        print "Energy: " + str(self.energy) + "  Score: " + str(self.score) + "\n"
        while True:
            action = raw_input("Hide(H)    Fly(F)     Search(S)    Attack(A)").lower()
            if action in ["h", "hide"]:
                owl.hide(name)
            elif action in ["f", "fly"]:
                owl.fly(name)
            elif action in ["s", "search"]:
                owl.search(name)
            elif action in ["a", "attack"]:
                owl.attack(name)
            else:
                print "\n", name, "didn't know what to do, and spent energy getting confused."
                self.energy -= 1
            self.score += 1
            if self.energy < 0:
                print "\nSadly,", name, "died. You got a score of:", str(self.score)
                return self.score
            print "Energy: " + str(self.energy) + "  Score: " + str(self.score) + "\n"
            if self.score >= 100:
                print name + " has lived the best life an owl could! You win!\n"


# Makes the loop for the program to keep going, getting the name for the owl, and asking if you want to retry.
while True:
    owl = snowy_owl()
    highScore = 0
    name = raw_input("Name your snowy owl: ").capitalize()
    score = owl.start(name)
    if score > highScore:
        highScore = score
        highName = name
    else:
        highName = "Nobody"
    yorn = raw_input("Would you like to try again? Yes(Y) or No(N)?\n").lower()
    if yorn in ["n", "no"]:
        print "Your highest score was " + str(highScore) + " with " + str(highName)
        break
