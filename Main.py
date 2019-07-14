import pygame
import Game
import dots         # Imports necessary libraries for pacman
import moveghost
import time

background = (0, 0, 0)  # Black color
pacman = pygame.image.load("resources/pacman.png")  # Imports a picture from a local library
pacman = pygame.transform.scale(pacman, (35, 35))  # Resizes the image on the screen
ghost = pygame.image.load("resources/redghost.png")
ghost = pygame.transform.scale(ghost, (45, 45))
num1 = pygame.image.load("resources/1.png")
num1 = pygame.transform.scale(num1, (100, 100))
num1blue = pygame.image.load("resources/1blu.png")
num1blue = pygame.transform.scale(num1blue, (100, 100))
num2 = pygame.image.load("resources/2.png")
num2 = pygame.transform.scale(num2, (100, 100))
num2blue = pygame.image.load("resources/2blu.png")
num2blue = pygame.transform.scale(num2blue, (100, 100))
num3 = pygame.image.load("resources/3.png")
num3 = pygame.transform.scale(num3, (100, 100))
num3blue = pygame.image.load("resources/3blu.png")
num3blue = pygame.transform.scale(num3blue, (100, 100))
lock = pygame.image.load("resources/lock.png")
lock = pygame.transform.scale(lock, (75, 75))
menu = pygame.image.load("resources/mainmenu.png")
menu = pygame.transform.scale(menu, (200, 75))
maze = pygame.image.load("resources/maze.png")
maze = pygame.transform.scale(maze, (600, 800))
mazeg = pygame.image.load("resources/mazeg.png")
mazeg = pygame.transform.scale(mazeg, (600, 800))
mazer = pygame.image.load("resources/mazer.png")
mazer = pygame.transform.scale(mazer, (600, 800))
dot = pygame.image.load("resources/dot.png")
dot = pygame.transform.scale(dot, (10, 10))
blue = pygame.image.load("resources/blueghost.png")
blue = pygame.transform.scale(blue, (45, 45))
pink = pygame.image.load("resources/pink.png")
pink = pygame.transform.scale(pink, (45, 45))
white = pygame.image.load("resources/whiteghost.png")
white = pygame.transform.scale(white, (45, 45))
vul = pygame.image.load("resources/vulghost.png")
vul = pygame.transform.scale(vul, (45, 45))
orange = pygame.image.load("resources/orange.png")
orange = pygame.transform.scale(orange, (45, 45))
bigdot = pygame.image.load("resources/dot.png")
bigdot = pygame.transform.scale(bigdot, (20, 20))
cherry = pygame.image.load("resources/cherry.png")
cherry = pygame.transform.scale(cherry, (30, 30))


pygame.init()  # Initializes all pygame libraries
pygame.font.init()  # initializes font module
font = pygame.font.Font("resources/prstart.ttf", 20)  # Sets a custom font
introfont = pygame.font.Font("resources/prstart.ttf", 27)
screen = pygame.display.set_mode((600, 900))  # Launches a screen with custom dimensions (600, 900)
screen.fill(background)  # Fills screen with background color (black)

done = False  # Creates variable done that will be used for ending the game

pygame.mixer.music.load("resources/pacintro.mp3")  # Starts playing music
pygame.mixer.music.play(0)  # Plays this music once

text = font.render("You have 3 lives!", 1, (255, 255, 255))  # Creates text
run3 = True  # Variable used for moving text

countup = 0
countleft = 0
countright = 0  # These variables will be used to measure how many times the image
countdown = 0   # has been rotated
prevRotate = "right"
checkpoint = dots.checkpoints
levelselect = False
levelsunlocked = 0
fontpx2 = 70
locked = 2
highscore1 = 0
testvar2 = []
highscore2 = 0
highscore3 = 0
level = 0
cherrycount = 4
numran = 0
numran2 = 0
numran3 = 0
numran4 = 0
cherries = []
cherrypoints = 0

def cpyArr(src):
    dest = []
    srclen = len(src)
    index = 0
    while index < srclen:
        dest.append(src[index])
        index += 1
    return dest
dotarray = cpyArr(dots.dotarrays)
cherryarray = cpyArr(dots.cherryarrays)
bigdotarray = cpyArr(dots.bigdotarrays)


def intro():
    global level
    global levelselect
    global fontpx2
    global x5
    global y5
    if levelselect is False:
        screen.fill(background)
        introtext = introfont.render("Welcome to Pacman!", 1, (255, 255, 255))
        screen.blit(introtext, (70, 40))
        introtext2 = font.render("Select a level", 1, (255, 255, 255))
        screen.blit(introtext2, (150, 140))
        introtext3 = font.render("Created By: Yousef Ahmed", 1, (240, 253, 52))
        introtext4 = font.render("Highscore (Level 1) = " + str(highscore1), 1, (255, 255, 255))
        introtext5 = font.render("Highscore (Level 2) = " + str(highscore2), 1, (255, 255, 255))
        introtext6 = font.render("Highscore (Level 3) = " + str(highscore3), 1, (255, 255, 255))
        if fontpx2 < 640:  # Moves font back and forth
            fontpx2 += .1
        if fontpx2 >= 640:
            fontpx2 = -460
        screen.blit(introtext3, (fontpx2, 640))
        screen.blit(introtext4, (70, 480))
        screen.blit(introtext5, (70, 520))
        screen.blit(introtext6, (70, 560))
        if levelsunlocked == 0:
            screen.blit(num1, (70, 300))
            screen.blit(num2, (250, 300))
            screen.blit(num3, (430, 300))
            levelrect1 = num1.get_rect()
            levelrect1 = levelrect1.move(70, 300)
            levelrect2 = num2.get_rect()
            levelrect2 = levelrect2.move(250, 300)
            levelrect3 = num2.get_rect()
            levelrect3 = levelrect3.move(430, 300)
            if levelrect1.collidepoint(mousepos):
                screen.blit(num1blue, (70, 300))
            if levelrect2.collidepoint(mousepos):
                screen.blit(num2blue, (250, 300))
            if levelrect3.collidepoint(mousepos):
                screen.blit(num3blue, (430, 300))
            if locked == 2:
                screen.blit(lock, (262, 310))
                screen.blit(lock, (442, 310))
            if locked == 1:
                screen.blit(lock, (442, 310))
        if pygame.mouse.get_pressed()[0] and levelrect1.collidepoint(mousepos) and locked <= 2:
            level = 1
            init()
        if pygame.mouse.get_pressed()[0] and levelrect2.collidepoint(mousepos) and locked <= 1:
            level = 2
            init()
        if pygame.mouse.get_pressed()[0] and levelrect3.collidepoint(mousepos) and locked >= 0:
            level = 3
            x5 = 242
            y5 = 358
            init()
    else:
        keepmov()
        updatepos()
        movefont()
        drawdots()
        moveghosts1()
        moveghosts1()
        moveghosts2()
        moveghosts2()
        moveghosts3()
        moveghosts3()
        moveghosts4()
        moveghosts4()
        if level == 3:
            moveghosts5()
            moveghosts5()
        checkcollision()
def init():
    global levelselect
    global fontpx2
    global locked
    global score
    global highscore1
    global highscore2
    global highscore3
    global lives
    global stop
    global run3
    global dotarray
    global cherryarray
    global bigdotarray
    global fontpx
    global fontpy
    global movepos
    global text
    global x
    global y
    global ran
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    global x5
    global y5
    global run6
    global run7
    global run8
    global run9
    global score
    global numran
    global numran2
    global numran3
    global numran4
    global cherrycount
    global cherrypoints
    global run10
    levelselect = True
    lives = 3
    stop = False
    run3 = True
    x = 282
    y = 430
    rotateright()
    fontpx = 200
    fontpy = 830
    movepos = ""
    text = font.render("You have " + str(lives) + " lives!", 1, (255, 255, 255))
    ran = 0
    x1 = 255
    y1 = 358
    x2 = 300
    y2 = 358
    x3 = 320
    y3 = 358
    x4 = 280
    y4 = 358
    x5 = 242
    y5 = 358
    run6 = True
    run7 = 0
    run8 = True
    run9 = 0
    run10 = 0
    numran = 0
    numran2 = 0
    numran3 = 0
    numran4 = 0
    cherrycount = 4
    cherrypoints = 0
    dotarray = cpyArr(dots.dotarrays)
    cherryarray = cpyArr(dots.cherryarrays)
    bigdotarray = cpyArr(dots.bigdotarrays)

def rotateup():
    global countup
    global countleft  # Creates global variables
    global countright
    global countdown
    countleft = 0
    countdown = 0  # Resets count
    countright = 0
    global pacman
    global prevRotate
    if prevRotate == "right":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 90)  # Rotates pacman 90 degrees counterclockwise
            countup += 1
            prevRotate = "up"  # Sets a prevrotate variable so that pacman will rotate teh correct amount of degrees
    elif prevRotate == "left":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 270)
            countup += 1
            prevRotate = "up"
    elif prevRotate == "down":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 180)
            countup += 1
            prevRotate = "up"
def rotateleft():
    global countup
    global countleft
    global countright
    global countdown
    countup = 0
    countdown = 0
    countright = 0
    global pacman
    global prevRotate
    if prevRotate == "right":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 180)
            countup += 1
            prevRotate = "left"
    elif prevRotate == "up":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 90)
            countup += 1
            prevRotate = "left"
    elif prevRotate == "down":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 270)
            countup += 1
            prevRotate = "left"

def rotatedown():
    global countup
    global countleft
    global countright
    global countdown
    countup = 0
    countleft = 0
    countright = 0
    global pacman
    global prevRotate
    if prevRotate == "right":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 270)
            countup += 1
            prevRotate = "down"
    elif prevRotate == "up":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 180)
            countup += 1
            prevRotate = "down"
    elif prevRotate == "left":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 90)
            countup += 1
            prevRotate = "down"
def rotateright():
    global countup
    global countleft
    global countright
    global countdown
    countup = 0
    countleft = 0
    countright = 1
    countdown = 0
    global pacman
    global prevRotate
    if prevRotate == "down":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 90)
            countup += 1
            prevRotate = "right"
    elif prevRotate == "up":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 270)
            countup += 1
            prevRotate = "right"
    elif prevRotate == "left":
        while countup < 1:
            pacman = pygame.transform.rotate(pacman, 180)
            countup += 1
            prevRotate = "right"
move = 1  # Creates a variable for how many pixels the ghosts will move
stop = False  # Creates a variable for ending the game when all the dots are collected
numrun = 0
set = 0
numcollect = 0
countdots = 0
ran = 0
test1 = True
pacout = Game.pacoutcoor

def drawdots():
    count = 0
    count2 = 0
    count3 = 0
    pacedge = []
    cherries = []
    global dotarray
    global pacedge
    global lives
    dotcenters = []
    for i in range (0, len(dotarray)):
        temp3 = dotarray[i]  # Makes an array of all dot coordinates
        temp2 = [temp3[0] + 5,temp3[1] + 5]  # Adds 5 to all dot coordinates
        dotcenters.append(temp2)  # Appends dot coordinates + 5 to dotcenters
    global numrun
    global set
    global numcollect
    global text
    global run3
    global fontpx
    global fontpy
    global stop
    global locked
    global ran
    global x
    global y
    global levelselect
    global score
    global highscore1
    global highscore2
    global highscore3
    global level
    global bigdotarray
    global cherrycount
    global numran
    global numran2
    global numran3
    global numran4
    global cherries
    global cherryarray
    global cherrypoints
    for i in range (0, len(dotarray)):
        screen.blit(dot, dotarray[count])  # This code draws all the dots based on the coordinates
        count += 1
    if level ==2 or level ==3:
        for i in range (0, len(cherryarray)):
            screen.blit(cherry, cherryarray[count2])  # This code draws all the cherries based on the coordinates
            count2 += 1
        for i in range (0, cherrycount):
            cherry1 = cherry.get_rect()
            cherry1 = cherry1.move(cherryarray[count3])
            cherries.append(cherry1)
            count3 += 1
        pacrect = pacman.get_rect()
        pacrect = pacrect.move(x, y)
        for i in range (0, cherrycount):
            if pacrect.colliderect(cherries[i]):
                if y < 300 and x < 300 and numran == 0:
                    position = cherryarray.index([81, 137])
                    del cherryarray[position]
                    cherrycount -= 1
                    numran += 1
                    cherrypoints += 100
                if y < 300 and x > 300 and numran2 == 0:
                    position = cherryarray.index([494, 143])
                    del cherryarray[position]
                    cherrycount -= 1
                    numran2 += 1
                    cherrypoints += 100
                if y > 300 and x < 300 and numran3 == 0:
                    position = cherryarray.index([68, 657])
                    del cherryarray[position]
                    cherrycount -= 1
                    numran3 += 1
                    cherrypoints += 100
                if y > 300 and x > 300 and numran4 == 0:
                    position = cherryarray.index([503, 655])
                    del cherryarray[position]
                    cherrycount -= 1
                    numran4 += 1
                    cherrypoints += 100
    for i in range (0, 136):
        arrayi = pacout[i]  # Makes a new array of pacman's outside coordinates
        temp = [x + arrayi[0], y + arrayi[1]]  # Adds x and y to coordinates because pacman's position is always changing
        pacedge.append(temp)
    intersect = [val for val in pacedge if val in dotcenters]  # Checks for overlapping values in both arrays (when pacman goes over a dot)
    if len(pacedge) == 20:  # Makes sure that the array does not get too long
        del pacedge[0]
    if len(intersect) >= 1:
        pos = dotcenters.index(intersect[0])  # Finds the position of the overlapping coordinates in the array
        numcollect += 1  # Adds 1 to number of dots collected
        del dotarray[pos]  # Deletes that coordinate from the array so that it will not be drawn again
    if len(dotarray) + len(bigdotarray) == 0:  # If user collects all the dots...
        fontpx = 200
        fontpy = 830
        screen.blit(menu, (195, 808))
        menurect = menu.get_rect()
        menurect = menurect.move(195, 808)
        if pygame.mouse.get_pressed()[0] and menurect.collidepoint(mousepos):
            levelselect = False
            if level == 1:
                if highscore1 <= score:
                    highscore1 = score
            if level == 2:
                if highscore2 <= score:
                    highscore2 = score
            if level == 3:
                if highscore3 <= score:
                    highscore3 = score
            cherryarray = dots.testvar3
            intro()
        score = 0
        x = 282
        y = 430
        text = font.render("", 1, (255, 255, 255))
        stop = True  # Freezes ghosts
        if ran == 0 and locked > 0:
            if level == 1:
                locked = 1
            elif level == 2:
                locked = 0
            ran += 1

    # 252 dots
    screen.blit(pacman, (x, y))  # Draws pacman
lives = 3
ghostsbad = True
def checkcollision():
    global pacedge
    global text
    global fontpx
    global fontpy
    global run3
    global lives
    global x
    global y
    global ghostsbad
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    global x5
    global y5
    global run6
    global run7
    global run8
    global run9
    global run10
    global numcollect
    global stop
    global highscore1
    global highscore2
    global highscore3
    global levelselect
    global numcollect
    global dotarray
    global score
    global bigdotarray
    global level
    global cherryarray
    bigdotcenters = []
    count = 0
    ghostcoors = moveghost.ghostcoor  # Imports array of ghost coordinates
    redghostedge = []
    blueghostedge = []
    pinkghostedge = []
    orangeghostedge = []
    whiteghostedge = []
    for i in range (0, len(bigdotarray)):
        screen.blit(bigdot, bigdotarray[count])  # Draws big dots
        count += 1
    for i in range (0, len(bigdotarray)):
        temp3 = bigdotarray[i]
        temp2 = [temp3[0] + 5,temp3[1] + 5]  # Adds 5 to create center of bigdots
        bigdotcenters.append(temp2)
    for i in range(0, len(ghostcoors)):
        arrayi = ghostcoors[i]
        temp = [x1 + arrayi[0], y1 + arrayi[1]] # Adds x,y coordinates to each term in the array because ghost is moving
        redghostedge.append(temp)
    for i in range(0, len(ghostcoors)):
        arraya = ghostcoors[i]
        temp6 = [x2 + arraya[0], y2 + arraya[1]]
        blueghostedge.append(temp6)
    for i in range(0, len(ghostcoors)):
        arrayb = ghostcoors[i]
        temp7 = [x3 + arrayb[0], y3 + arrayb[1]]
        pinkghostedge.append(temp7)
    for i in range(0, len(ghostcoors)):
        arrayc = ghostcoors[i]
        temp8 = [x4 + arrayc[0], y4 + arrayc[1]]
        orangeghostedge.append(temp8)
    if level == 3:
        for i in range(0, len(ghostcoors)):
            arrayg = ghostcoors[i]
            temp9 = [x5 + arrayg[0], y5 + arrayg[1]]
            whiteghostedge.append(temp9)
    intersect2 = [val for val in pacedge if val in redghostedge]  # Checks for overlapping values of pacman and the ghost array
    intersect3 = [val for val in pacedge if val in blueghostedge]
    intersect4 = [val for val in pacedge if val in pinkghostedge]
    intersect5 = [val for val in pacedge if val in orangeghostedge]
    intersect6 = [val for val in pacedge if val in bigdotcenters]  # Checks for overlap in pacman's edge and bigdot centers
    if level == 3:
        intersect7 = [val for val in pacedge if val in whiteghostedge]
    if len(intersect6) >= 1:
        pos = bigdotcenters.index(intersect6[0])
        ghostsbad = False
        del bigdotarray[pos]  # Deletes big dot from array so that it will not be drawn again
        numcollect += 1
        start = time.time()  # Starts a timer
        global start
    if len(redghostedge) == 20:
        del redghostedge[0]
    if len(blueghostedge) == 20:
        del blueghostedge[0]  # Ensures that length of arrays is not too long
    if len(pinkghostedge) == 20:
        del pinkghostedge[0]
    if len(orangeghostedge) == 20:
        del orangeghostedge[0]
    if level == 3:
        if len(whiteghostedge) == 20:
            del whiteghostedge[0]
    if len(intersect2) >= 1 or len(intersect3) >= 1 or len(intersect4) >= 1 or len(intersect5) >= 1:  # If there are overlapping values, it will run this code
        if ghostsbad is True:  # To make sure that user still has not collected big dot
            x = 282  # Resets pacman to starting position
            y = 430
            lives -= 1
            text = font.render("You have " + str(lives) + " lives!", 1, (255, 255, 255))  # Renders text to equal number of lives of pacman
        elif ghostsbad is False:
            if len(intersect2) >= 1:
                x1 = 255
                y1 = 358
            elif len(intersect3) >= 1:
                x2 = 300
                y2 = 358  # This code resets ghosts to starting position
            elif len(intersect4) >= 1:
                x3 = 320
                y3 = 358
                run6 = True
                run7 = 0
            elif len(intersect5) >= 1:
                x4 = 280
                y4 = 358
                run8 = True
                run9 = 0
    if level == 3:
        if len(intersect7) >= 1:
            if ghostsbad is True:  # To make sure that user still has not collected big dot
                x = 282  # Resets pacman to starting position
                y = 430
                lives -= 1
                text = font.render("You have " + str(lives) + " lives!", 1, (255, 255, 255))  # Renders text to equal number of lives of pacman
            elif ghostsbad is False:
                if len(intersect7) >= 1:
                    x5 = 255
                    y5 = 358
                    run10 = 0
    if ghostsbad is False:
        if time.time() - start < 15:  # Calculates time elapsed and only runs while it is less than 15
            screen.blit(vul, (x1, y1))
            screen.blit(vul, (x2, y2))
            screen.blit(vul, (x3, y3))  # Draws blue ghost over regular ghosts
            screen.blit(vul, (x4, y4))
            if level == 3:
                screen.blit(vul, (x5, y5))
        if time.time() - start > 15:
            ghostsbad = True  # Resets ghosts to regular

    if lives == 1:
        text = font.render("You have " + str(lives) + " life!", 1, (255, 255, 255))
    if lives == 0:
        fontpx = 200
        fontpy = 400  # Moves text to center

        run3 = False
        stop = True
        screen.fill(background)  # Draws a black background
        text = font.render("GAME OVER!", 1, (255, 255, 255))
        text2 = font.render("Score:" + str(score), 1, (255, 255, 255))
        screen.blit(text, (fontpx, fontpy))
        screen.blit(text2, (210, 460))
        screen.blit(menu, (195, 808))
        menurect = menu.get_rect()
        menurect = menurect.move(195, 808)
        if pygame.mouse.get_pressed()[0] and menurect.collidepoint(mousepos):
            levelselect = False
            if level == 1:
                if highscore1 <= score:
                    highscore1 = score
            if level == 2:
                if highscore2 <= score:
                    highscore2 = score
            if level == 3:
                if highscore3 <= score:
                    highscore3 = score
            dotarray = dots.dotarrays
            cherryarray = dots.testvar3
            intro()
        score = 0

x = 282
y = 430

x1 = 255
y1 = 358

x2 = 300
y2 = 358  # Ghosts and pacman coordinates

x3 = 320
y3 = 358

x4 = 280
y4 = 358

x5 = 242
y5 = 358

fontpx = 200
fontpy = 830

run2 = True
run4 = True
run5 = True
run6 = True
run7 = 0
run8 = True
run9 = 0
run10 = 0

def moveghosts1():
    global x1
    global y1
    global move
    global run2
    global stop
    if stop is True:
        return  # Stop is used to freeze ghosts
    elif x1 <= 278 and y1 == 358:
        x1 += move
        screen.blit(ghost, (x1, y1))
    elif y1 >= 280:
        y1 -= move
        screen.blit(ghost, (x1, y1))  # Moves ghosts in a set pattern
    elif x1 > 128 and y1 == 279 and run2 is True:
        x1 -= move
        screen.blit(ghost, (x1, y1))
        if x1 == 128:
            run2 = False
    elif x1 < 425 and y1 == 279 and run2 is False:
        x1 += move
        screen.blit(ghost, (x1, y1))
        if x1 == 425:
            run2 = True
def moveghosts2():
    global x2
    global y2
    global move
    global run4
    global run5
    global stop
    global movepos
    if stop is True:
        return
    elif x2 >= 278 and y2 == 358:
        x2 -= move
        screen.blit(blue, (x2, y2))
    elif y2 >= 280 and x2 == 277:
        y2 -= move
        screen.blit(blue, (x2, y2))
    elif x2 > 124 and y2 == 279 and run5 is True:
        x2 -= move
        screen.blit(blue, (x2, y2))
        if x == 124:
            run5 = False
    elif x2 == 124 and y2 > 20 and run4 is True:
        y2 -= move
        screen.blit(blue, (x2, y2))
        if y2 == 20:
            run4 = False
    elif x2 == 124 and y2 < 728 and run4 is False:
        y2 += move
        screen.blit(blue, (x2, y2))
        if y2 == 728:
            run4 = True

def moveghosts3():
    global x3
    global y3
    global move
    global run6
    global run7
    global stop
    if stop is True:
        return
    elif x3 >= 278 and y3 == 358 and run6 is True:
        x3 -= move
        screen.blit(pink, (x3, y3))
    elif y3 >= 280 and x3 == 277 and run6 is True:
        y3 -= move
        screen.blit(pink, (x3, y3))
    elif x3 < 435 and y3 == 279 and run6 is True:
        x3 += move
        screen.blit(pink, (x3, y3))
    elif y3 > 25 and x3 == 435 and run7 == 0:
        y3 -= move
        screen.blit(pink, (x3, y3))
        if y3 == 25:
            run6 = False
            run7 = 1
    elif y3 < 500 and x3 == 435 and run7 == 1:
        y3 += move
        screen.blit(pink, (x3, y3))
        if y3 == 500:
            run7 = 2
    elif x3 > 25 and y3 == 500 and run7 == 2:
        x3 -= move
        screen.blit(pink, (x3, y3))
        if x3 == 25:
            run7 = 3
    elif x3 < 435 and y3 == 500 and run7 == 3:
        x3 += move
        screen.blit(pink, (x3, y3))
        if x3 == 435:
            run7 = 0
def moveghosts4():
    global x4
    global y4
    global move
    global run8
    global run9
    global stop
    if stop is True:
        return
    elif x4 >= 278 and y4 == 358 and run8 is True:
        x4 -= move
        screen.blit(orange, (x4, y4))
    elif y4 >= 280 and x4 == 277 and run8 is True:
        y4 -= move
        screen.blit(orange, (x4, y4))
    elif x4 < 435 and y4 == 279 and run8 is True:
        x4 += move
        screen.blit(orange, (x4, y4))
    elif y4 < 728 and x4 == 435 and run9 == 0:
        y4 += move
        screen.blit(orange, (x4, y4))
        run8 = False
        if y4 == 728:
            run9 = 1
    elif x4 > 25 and y4 == 728 and run9 == 1:
        x4 -= move
        screen.blit(orange, (x4, y4))
        if x4 == 25:
            run9 = 2
    elif y4 > 658 and x4 == 25 and run9 == 2:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 658:
            run9 = 3
    elif x4 < 62 and y4 == 658 and run9 == 3:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 62:
            run9 = 4
    elif y4 > 573 and x4 == 62 and run9 == 4:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 573:
            run9 = 5
    elif x4 > 23 and y4 == 573 and run9 == 5:
        x4 -= move
        screen.blit(orange, (x4, y4))
        if x4 == 23:
            run9 = 6
    elif y4 > 506 and x4 == 23 and run9 == 6:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 506:
            run9 = 7
    elif x4 < 66 and y4 == 506 and run9 == 7:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 66:
            run9 = 8
    elif y4 > 434 and x4 == 66 and run9 == 8:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 434:
            run9 = 9
    elif x4 > 25 and y4 == 434 and run9 == 9:
        x4 -= move
        screen.blit(orange, (x4, y4))
        if x4 == 25:
            run9 = 10
    elif y4 > 281 and x4 == 25 and run9 == 10:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 281:
            run9 = 11
    elif x4 < 64 and y4 == 281 and run9 == 11:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 64:
            run9 = 12
    elif y4 > 208 and x4 == 64 and run9 == 12:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 208:
            run9 = 13
    elif x4 > 25 and y4 == 208 and run9 == 13:
        x4 -= move
        screen.blit(orange, (x4, y4))
        if x4 == 25:
            run9 = 14
    elif y4 > 32 and x4 == 25 and run9 == 14:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 32:
            run9 = 15
    elif x4 < 249 and y4 == 32 and run9 == 15:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 249:
            run9 = 16
    elif y4 < 71 and x4 == 249 and run9 == 16:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 71:
            run9 = 17
    elif x4 < 309 and y4 == 71 and run9 == 17:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 309:
            run9 = 18
    elif y4 > 30 and x4 == 309 and run9 == 18:
        y4 -= move
        screen.blit(orange, (x4, y4))
        if y4 == 30:
            run9 = 19
    elif x4 < 536 and y4 == 30 and run9 == 19:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 536:
            run9 = 20
    elif y4 < 201 and x4 == 536 and run9 == 20:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 201:
            run9 = 21
    elif x4 > 495 and y4 == 201 and run9 == 21:
        x4 -= move
        screen.blit(orange, (x4, y4))
        if x4 == 495:
            run9 = 22
    elif y4 < 280 and x4 == 495 and run9 == 22:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 280:
            run9 = 23
    elif x4 < 536 and y4 == 280 and run9 == 23:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 536:
            run9 = 24
    elif y4 < 424 and x4 == 536 and run9 == 24:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 424:
            run9 = 25
    elif x4 > 497 and y4 == 424 and run9 == 25:
        x4 -= move
        screen.blit(orange, (x4, y4))
        if x4 == 497:
            run9 = 26
    elif y4 < 500 and x4 == 497 and run9 == 26:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 500:
            run9 = 27
    elif x4 < 538 and y4 == 500 and run9 == 27:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 538:
            run9 = 28
    elif y4 < 575 and x4 == 538 and run9 == 28:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 575:
            run9 = 29
    elif x4 > 499 and y4 == 575 and run9 == 29:
        x4 -= move
        screen.blit(orange, (x4, y4))
        if x4 == 499:
            run9 = 30
    elif y4 < 646 and x4 == 499 and run9 == 30:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 646:
            run9 = 31
    elif x4 < 538 and y4 == 646 and run9 == 31:
        x4 += move
        screen.blit(orange, (x4, y4))
        if x4 == 538:
            run9 = 32
    elif y4 < 728 and x4 == 538 and run9 == 32:
        y4 += move
        screen.blit(orange, (x4, y4))
        if y4 == 728:
            run9 = 1
def moveghosts5():
    global x5
    global y5
    global move
    global run10
    global stop
    if stop is True:
        return  # Stop is used to freeze ghosts
    elif x5 <= 278 and y5 == 358:
        x5 += move
        screen.blit(white, (x5, y5))
    elif y5 >= 280:
        y5 -= move
        screen.blit(white, (x5, y5))  # Moves ghosts in a set pattern
    elif x5 > 128 and y5 == 279:
        x5 -= move
        screen.blit(white, (x5, y5))
    elif y5 > 130 and x5 == 128:
        y5 -= move
        screen.blit(white, (x5, y5))
    elif x5 < 247 and y5 == 130 and run10 == 0:
        x5 += move
        screen.blit(white, (x5, y5))
        if x5 == 247:
            run10 = 1
    elif y5 > 81 and x5 == 247 and run10 == 1:
        y5 -= move
        screen.blit(white, (x5, y5))
        if y5 == 81:
            run10 = 2
    elif x5 < 310 and y5 == 81 and run10 == 2:
        x5 += move
        screen.blit(white, (x5, y5))
        if x5 == 310:
            run10 = 3
    elif y5 < 125 and x5 == 310 and run10 == 3:
        y5 += move
        screen.blit(white, (x5, y5))
        if y5 == 125:
            run10 = 4
    elif x5 < 370 and y5 == 125 and run10 == 4:
        x5 += move
        screen.blit(white, (x5, y5))
        if x5 == 370:
            run10 = 5
    elif y5 < 197 and x5 == 370 and run10 == 5:
        y5 += move
        screen.blit(white, (x5, y5))
        if y5 == 197:
            run10 = 6
    elif x5 > 303 and y5 == 197 and run10 == 6:
        x5 -= move
        screen.blit(white, (x5, y5))
        if x5 == 303:
            run10 = 7
    elif y5 < 278 and x5 == 303 and run10 == 7:
        y5 += move
        screen.blit(white, (x5, y5))
        if y5 == 278:
            run10 = 8
    elif x5 > 242 and y5 == 278 and run10 == 8:
        x5 -= move
        screen.blit(white, (x5, y5))
        if x5 == 242:
            run10 = 9
    elif y5 > 199 and x5 == 242 and run10 == 9:
        y5 -= move
        screen.blit(white, (x5, y5))
        if y5 == 199:
            run10 = 10
    elif x5 > 187 and y5 == 199 and run10 == 10:
        x5 -= move
        screen.blit(white, (x5, y5))
        if x5 == 187:
            run10 = 11
    elif y5 > 130 and x5 == 187 and run10 == 11:
        y5 -= move
        screen.blit(white, (x5, y5))
        if y5 == 130:
            run10 = 0
def movefont():
    global fontpx
    global fontpy
    global run3
    if fontpx < 640 and run3 is True:  # Moves font back and forth
        fontpx += 1
    if fontpx == 640 and run3 is True:
        fontpx = -350

intersect = []
realcoors = Game.coors
pos = ""
canmove = True
movepos = 0
def keepmov():
    global pos
    global x
    global y
    global intersect
    if pos == "left":
        x -= 1
    elif pos == "right":
        x += 1
    elif pos == "down":
        y += 1
    elif pos == "up":
        y -= 1
def moveleft():
    global x
    global y
    global pos
    if movepos == 2:
        rotateleft()  # rotates pacman to the left
        pos = "left"
def moveup():
    global movepos
    global pos
    if movepos == 1:
        pos = "up"
        rotateup()
def moveright():
    global pos
    if movepos == 4:
        pos = "right"
        rotateright()
def movedown():
    global pos
    if movepos == 3:
        pos = "down"
        rotatedown()
lastcoorx = []  # arrays used to store last coordinates of pacman
lastcoory = []
run = 0
def updatepos():
    global xcoor
    global ycoor
    global pacman
    global x
    global y
    global lastcoorx
    global lastcoory
    global run
    global done
    global intersect
    global canmove
    global movepos
    global level
    screen.blit(maze, (0, 0))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:  # Closes game if escape is pressed
            done = True
        if event.key == pygame.K_RIGHT:
            movepos = 4
            moveright()
        if event.key == pygame.K_LEFT:
            movepos = 2
            moveleft()
        if event.key == pygame.K_UP:
            movepos = 1
            moveup()
        if event.key == pygame.K_DOWN:
            movepos = 3
            movedown()
    else:
        moveright()
        movedown()  # Allows movement
        moveup()
        moveleft()
    if len(lastcoorx) > 5:  # Limits length of last coor x
        del lastcoorx[0]
        del lastcoory[0]
    topleft = [x+5, y+5]
    topright = [x+31, y+5]
    bottomleft = [x+5, y+31]  # Corners of pacman
    bottomright = [x+31, y+31]
    lastcoorx.append(x)
    lastcoory.append(y)
    if topleft in realcoors or topright in realcoors or bottomleft in realcoors or bottomright in realcoors:  # Detects intersection with boundary
        length = len(lastcoorx)
        del lastcoorx[length - 1]  # Deletes bad coordinate from lastcoor
        del lastcoory[length - 1]
        length -= 6
        x = lastcoorx[length]  # Resets pacman to a previous position
        y = lastcoory[length]
    else:
        moveright()
        movedown()  # Allows movement
        moveup()
        moveleft()
    screen.fill(background)
    if level == 1:
        screen.blit(maze, (0, 0))
    elif level == 2:
        screen.blit(mazeg, (0, 0))
    elif level == 3:
        screen.blit(mazer, (0, 0))
    screen.blit(pacman, (x, y))
    screen.blit(pink, (x3, y3))
    screen.blit(blue, (x2, y2))
    screen.blit(orange, (x4, y4))
    screen.blit(ghost, (x1, y1))
    if level == 3:
        screen.blit(white, (x5, y5))
    screen.blit(text, (fontpx, fontpy))

while not done:
    for event in pygame.event.get():  # Event listener
        if event.type == pygame.QUIT:  # Runs when window is closed
            done = True
    score = 252 - len(dotarray) - len(bigdotarray)
    score += cherrypoints
    print(len(dotarray) + len(bigdotarray))
    mousepos = pygame.mouse.get_pos()
    intro()
    pygame.display.flip()  # Buffers screen





