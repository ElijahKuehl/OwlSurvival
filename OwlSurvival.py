from appJar import gui
from random import randint


flying = False
hiding = False
target = False
energy = 5
score = 0
highScore = 0
highName = "Ali"
win = True
predator = False


def press(button):
    global flying, hiding, target, energy, score, highScore, highName, win, predator
    if button == "Start" or button == "Try Again":
        start()

    elif button == "Hide":
        if not flying:
            app.setImage("Owl", "Owl Hiding.jpg")
            app.shrinkImage("Owl", 3)
            app.setImageSize("Owl", 300, 225)
            app.hideButton("Hide")
            app.showButton("Unhide")
            energy -= 1
            score += 1
            app.setLabel("Happen", name + " hid deep into the snow.\n")
            app.setLabel("EnergyScore", "Energy: " + str(energy) + "  Score: " + str(score))
            hiding = True
        else:
            app.setLabel("Happen", "You are too high up to hide!\n")

        if score == 1 and energy == 3 and flying and name == "Ali":
            energy = 99
            app.setLabel("Happen", "The luck of the Official Test Owl Ali is with you!\n")
            app.setImage("Owl", "Ali Owl.jpg")
            app.shrinkImage("Owl", 6)
            app.setLabel("EnergyScore", "Energy: " + str(energy) + "  Score: " + str(score))

    elif button == "Unhide":
        app.setImage("Owl", "Standing Owl.jpg")
        app.shrinkImage("Owl", 5)
        app.setImageSize("Owl", 320, 200)
        app.hideButton("Unhide")
        app.showButton("Hide")
        score += 1
        app.setLabel("Happen", name + " came out of the snow.\n")
        app.setLabel("EnergyScore", "Energy: " + str(energy) + "  Score: " + str(score))
        hiding = False

    elif button == "Fly":
        if hiding:
            app.setLabel("Happen", name + " came out of the snow.\n")
            app.hideButton("Unhide")
            app.showButton("Hide")
        app.setImage("Owl", "Owl Flying.jpg")
        app.setLabel("Happen", name + " flew into the air!\n")
        app.shrinkImage("Owl", 2)
        app.setImageSize("Owl", 320, 200)
        app.hideButton("Fly")
        app.showButton("Land")
        energy -= 2
        score += 1
        app.setLabel("EnergyScore", "Energy: " + str(energy) + "  Score: " + str(score))
        flying = True

    elif button == "Land":
        app.setImage("Owl", "Standing Owl.jpg")
        app.setLabel("Happen", name + " glided to the ground.\n")
        app.shrinkImage("Owl", 5)
        app.setImageSize("Owl", 320, 200)
        app.hideButton("Land")
        app.showButton("Fly")
        flying = False

    elif button == "Search":
        if flying:
            accuracy = 2
            app.setLabel("Happen", name + " looks onto the ground... ")
        elif not flying:
            accuracy = 3
            app.setLabel("Happen", name + " looks across the ground... ")
        else:
            accuracy = 1
        search = randint(1, accuracy)
        if search == 1:
            app.setLabel("Happen", name + " found a mouse! Go in for the Attack!\n")
            app.setImage("Owl", "Mouse found.jpg")
            app.shrinkImage("Owl", 5)
            app.setImageSize("Owl", 320, 200)
            app.hideButton("Search")
            app.showButton("Attack")
        else:
            app.setLabel("Happen", name + " didn't find anything.\n")
            app.setImage("Owl", "Search Fail.jpg")
            app.shrinkImage("Owl", 2)
            app.setImageSize("Owl", 320, 200)
            energy -= 1
            score += 1
        app.setLabel("EnergyScore", "Energy: " + str(energy) + "  Score: " + str(score))

    elif button == "Attack":
        skill = 0
        if hiding:
            app.setLabel("Happen", name + " came out of the snow.\n")
            hiding = False
            app.hideButton("Unhide")
            app.showButton("Hide")
            skill -= 1
        if flying:
            app.setLabel("Happen", name + " dives... ")
            skill += 2
            chance = randint(1, skill)
            flying = False
            app.hideButton("Land")
            app.showButton("Fly")
        else:
            app.setLabel("Happen", name + " creeps up to the target... ")
            skill += 3
            chance = randint(1, skill)
        if chance == 1:
            app.setLabel("Happen", name + " caught the mouse!\n")
            app.setImage("Owl", "Owl Catch.jpg")
            app.shrinkImage("Owl", 5)
            energy += 5
        else:
            app.setLabel("Happen", name + " Missed the mouse!\nThe mouse got away!\n")
            app.setImage("Owl", "Hunt Fail.jpg")
            app.shrinkImage("Owl", 2)
        app.setImageSize("Owl", 320, 200)
        app.hideButton("Attack")
        app.showButton("Search")
        energy -= 1
        score += 1
        app.setLabel("EnergyScore", "Energy: " + str(energy) + "  Score: " + str(score))

    elif button == "Quit":
        app.infoBox("High Score",
                    "Your highest score was " + str(highScore) + " with " + highName)
        app.stop()

    if predator:
        if flying:
            app.setLabel("Fox", "The fox couldn't get to you!")
            predator = False
        else:
            live = 3
            if hiding:
                live = 5
            survive = randint(1, live)
            if survive == 1:
                app.setLabel("Fox", "The fox caught you!")
                app.setImage("Owl", "Lose.jpg")
                app.shrinkImage("Owl", 3)
                death = "Sadly, " + name + " died. " + name + " got a score of: " + str(score) + "\n"
                app.setLabel("Happen", death)
                app.infoBox("Lose", death)
                app.hideButton("Hide")
                app.hideButton("Fly")
                app.hideButton("Search")
                app.hideButton("Unhide")
                app.hideButton("Land")
                app.hideButton("Attack")
                predator = False
            else:
                app.setLabel("Fox", "Luckily, the fox didn't see " + name)
                predator = False
    else:
        try:
            app.setLabel("Fox", "")
        except Exception:
            pass

    try:
        if energy < 0:
            app.setImage("Owl", "Lose.jpg")
            app.shrinkImage("Owl", 3)
            death = "Sadly, " + name + " died. " + name + " got a score of: " + str(score) + "\n"
            app.setLabel("Happen", death)
            app.infoBox("Lose", death)
            app.hideButton("Hide")
            app.hideButton("Fly")
            app.hideButton("Search")
            app.hideButton("Unhide")
            app.hideButton("Land")
            app.hideButton("Attack")
    except Exception:
        pass

    if score > highScore:
        highScore = score
        highName = name

    if score >= 100 and win:
        win = False
        app.setImage("Owl", "Win.jpg")
        app.shrinkImage("Owl", 3)
        app.setImageSize("Owl", 320, 250)
        win = name + " has lived the best life an owl could! You win!\n"
        app.setLabel("Happen", win)
        app.infoBox("Victory!", win)

    fox = randint(1, 10)
    if fox == 1:
        app.setLabel("Fox", "A wild fox appeared!")
        predator = True


def start():
    global flying, hiding, target, energy, score, highScore, highName, win, predator, name
    app.hideButton("Start")
    app.hideButton("Unhide")
    app.hideButton("Land")
    app.hideButton("Attack")
    app.showButton("Try Again")
    app.showButton("Hide")
    app.showButton("Fly")
    app.showButton("Search")
    app.setImage("Owl", "Standing Owl.jpg")
    app.shrinkImage("Owl", 5)
    app.setImageSize("Owl", 320, 200)
    flying = False
    hiding = False
    target = False
    energy = 5
    score = 0
    win = True
    predator = False
    app.setLabel("Fox", "")
    app.setLabel("Happen", "")
    app.setLabel("EnergyScore", "Energy: " + str(energy) + "  Score: " + str(score))

    while True:
        name = app.stringBox("Name", "Name your owl")
        name = name.capitalize()
        if name not in ["", " ", "  ", "   ", "    "] or "     " not in name:
            break
        else:
            app.infoBox("Empty Name", "Must have a name")
    app.setLabel("Happen", "What would you like " + name + " to do?\n")


app = gui("Owl Survival", "750x500")
app.setBg("#EFEFEF")
app.setFont(18)

ok = app.okBox("Loading Images", "We will be loading images. This may take awhile.")
if not ok:
    app.stop()

app.addImage("Owl", "Owl Hiding.jpg")
app.setImage("Owl", "Lose.jpg")
app.setImage("Owl", "Win.jpg")
app.setImage("Owl", "Hunt Fail.jpg")
app.setImage("Owl", "Owl Catch.jpg")
app.setImage("Owl", "Owl Flying.jpg")
app.setImage("Owl", "Mouse found.jpg")
app.setImage("Owl", "Search Fail.jpg")
app.setImage("Owl", "Standing Owl.jpg")
app.shrinkImage("Owl", 5)
app.setImageSize("Owl", 320, 200)

app.addLabel("EnergyScore", "Energy: 0  Score: 0")

app.addButtons(["Hide", "Fly", "Search"], press)
app.addButtons(["Unhide", "Land", "Attack"], press)
app.setButtonBg("Attack", "#FF0000")
app.hideButton("Hide")
app.hideButton("Fly")
app.hideButton("Search")
app.hideButton("Attack")
app.hideButton("Unhide")
app.hideButton("Land")

app.addLabel("Happen", "")

app.addLabel("Fox", "")

app.addButtons(["Start", "Try Again", "Quit"], press)
app.hideButton("Try Again")

app.go()
