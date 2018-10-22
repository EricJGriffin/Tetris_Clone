# Tetris.py
from graphics import *
from square import Square
import math
from random import randrange
from random import random
from pole import Pole
from tshape import Tshape
from rknight import Rknight
from lknight import Lknight
from rhorse import Rhorse
from lhorse import Lhorse
from minishapes import *
from button import Button
import winsound
from pygame import *
###############################################################################
""" This is a Tetris clone."""
songs = ['Highway Slaughter.ogg', 'Tetris.ogg']
def main():
    win = makeGrid()
    grid = Data(win)
    pauseButton = Button(win, Point(1,6), 0.8, 0.6, "Pause")
    pauseButton.activate()
    quitButton = Button(win, Point(1, 5), 0.8, 0.6, "Quit")
    quitButton.setFill('darkgrey')
    quitButton.activate()
    oList = []
    Level = 1
    Score = 0
    compLines = 0
    levLabel = Text(Point(2.7, 7.5), "Level:").draw(win)
    levLabel.setStyle("bold")
    scoreLabel = Text(Point(3.7, 7.5), "Score:").draw(win)
    scoreLabel.setStyle("bold")
    dispLevel = Text(Point(3.2, 7.5), Level).draw(win)
    dispLevel.setStyle("bold")
    dispScore = Text(Point(4.2, 7.5), Score).draw(win)
    dispScore.setStyle("bold")
    displayHighScores(win)
    
    n = 17  + (Level - 1) * 3 # start at 17. n will be adjusted to change the speed of the falling objects
    global songs
    mixer.init()
    mixer.music.load(songs[0])
    mixer.music.play()
    currentlyPlaying = songs[0]

    while not GameOver(grid):
        currentlyPlaying = playNextSong(currentlyPlaying)
        currentObject, oList = nextThree(oList)# selects the next three shapes
        ob1, ob2, ob3 = displayNext(oList, win) # displays the next three shapes
        consecRows = objGen(currentObject, win, grid, pauseButton, quitButton, n) # objGen animates the shape falling
        compLines = compLines + consecRows # consecRows is the amount of consecutive completed rows after a single instance of objGen
        Level, Score, compLines = scoreAndLevelAdjuster(Level, Score, compLines, consecRows)
        
        oList.remove(oList[0])
        ob1.undraw()
        ob2.undraw()
        ob3.undraw()
        dispLevel.setText(Level)
        dispScore.setText(Score)
        n = 17 + (Level - 1) * 3



    adjustHighScores(win, Score)    
    label = Text(Point(3.5, 0.2), "GAME OVER...Click anywhere to quit").draw(win)
    label.setStyle("bold")
    win.getMouse()
    mixer.music.stop()
    win.close()
################################################################################
def playNextSong(currentlyPlaying):
    global songs
            
    if not mixer.music.get_busy():
        if currentlyPlaying == songs[0]:
            mixer.music.load(songs[1])
            mixer.music.play(2)
            currentlyPlaying = songs[1]
        elif currentlyPlaying == songs[1]:
            mixer.music.load(songs[0])
            mixer.music.play()
            currentlyPlaying = songs[0]
    return currentlyPlaying
        

################################################################################
def displayHighScores(win):

    hScoreLabel = Text(Point(6.0, 4.5), "Top 5 High Scores").draw(win)
    hScoreLabel.setSize(16)
    hScoreLabel.setStyle("bold")
    infile = open("HighScores.txt", "r")
    HSNamex = 5.6 # high score name x
    HSScorex = 6.3 # high score score x
    HSy = 4.0 # high score y
    for i, line in enumerate(infile):
        if i < 5:
            name, hScore = line.split()
            Text(Point(HSNamex, HSy), name).draw(win)
            Text(Point(HSScorex, HSy), hScore).draw(win)
            HSy = HSy - 0.4    
    infile.close()
###############################################################################
def adjustHighScores(win, Score):

    infile = open("HighScores.txt", "r")
    scoreDict = {}
    found = False
    index = 0
    newName = ""
    test = infile.readline()
    infile.close()
    infile = open("HighScores.txt", "r")
    
    if len(test) == 0:
        newName = getName()
    elif len(test) != 0:
        for i, line in enumerate(infile):
            name, hScore = line.split()
            if (Score >= int(hScore)) and (i < 5) and (found == False):
                found = True
                index = i
                newName = getName()
    infile.close()
    infile = open("HighScores.txt", "r")
    contents = infile.readlines()
    infile.close()
    contents.insert(index, newName + " " + str(Score) + "\n")

    infile = open("HighScores.txt", "w")
    contents = "".join(contents)
    infile.write(contents)
    infile.close()
################################################################################
def getName():
    newWin = GraphWin("Enter Name", 300, 200)
    newWin.setBackground("yellow")
    newWin.setCoords(0,0,2,2)
    Text(Point(1,1.65), "Congratulations! You have a high score!").draw(newWin)
    Text(Point(1,1.4), "Enter your name (first)").draw(newWin)
    inputBox = Entry(Point(1, 1), 10).draw(newWin)
    submit = Button(newWin, Point(1, 0.5), 0.7, 0.5, "Submit")
    submit.activate()
    while True:
        pt = newWin.checkMouse()
        if type(pt) == Point:
            if submit.clicked(pt):
                newName = inputBox.getText()
                newWin.close()
                break    
    return newName
################################################################################    
def GameOver(grid):
    x = 2.15
    for row in range(10):
        if grid[6.65][x][2] == True:
            return True
        x = round(x + 0.30, 2)
    return False


#####################################################################################
def scoreAndLevelAdjuster(Level, Score, compLines, consecRows):

    if consecRows == 1:
        Score = Score + (100 * Level)
    elif consecRows == 2:
        Score = Score + (300 * Level)
    elif consecRows == 3:
        Score = Score + (500 * Level)
    elif consecRows == 4:
        Score = Score + (800 * Level)

    if compLines >= 10:
        Level = Level + 1
        compLines = compLines % 10

        
    return Level, Score, compLines
        
################################################################################
# selects the next three objects randomly    
def nextThree(oList):
    while len(oList) < 4:
        oList.append(randomObject())
    return oList[0], oList
################################################################################
# displays the next three objects
def displayNext(oList, win):
    c1 = Point(6.0, 6.6)
    c2 = Point(6.0, 6.2)
    c3 = Point(6.0, 5.8)
    if oList[1] == "square":
        shape1 = miniSquare(c1)
    elif oList[1] == "Tshape":
        shape1 = miniTshape(c1)
    elif oList[1] == "pole":
        shape1 = miniPole(c1)
    elif oList[1] == "Rknight":
        shape1 = miniRknight(c1)
    elif oList[1] == "Lknight":
        shape1 = miniLknight(c1)
    elif oList[1] == "Rhorse":
        shape1 = miniRhorse(c1)
    elif oList[1] == "Lhorse":
        shape1 = miniLhorse(c1)

    if oList[2] == "square":
        shape2 = miniSquare(c2)
    elif oList[2] == "Tshape":
        shape2 = miniTshape(c2)
    elif oList[2] == "pole":
        shape2 = miniPole(c2)
    elif oList[2] == "Rknight":
        shape2 = miniRknight(c2)
    elif oList[2] == "Lknight":
        shape2 = miniLknight(c2)
    elif oList[2] == "Rhorse":
        shape2 = miniRhorse(c2)
    elif oList[2] == "Lhorse":
        shape2 = miniLhorse(c2)

    if oList[3] == "square":
        shape3 = miniSquare(c3)
    elif oList[3] == "Tshape":
        shape3 = miniTshape(c3)
    elif oList[3] == "pole":
        shape3 = miniPole(c3)
    elif oList[3] == "Rknight":
        shape3 = miniRknight(c3)
    elif oList[3] == "Lknight":
        shape3 = miniLknight(c3)
    elif oList[3] == "Rhorse":
        shape3 = miniRhorse(c3)
    elif oList[3] == "Lhorse":
        shape3 = miniLhorse(c3)
    
    shape1.draw(win)
    shape2.draw(win)
    shape3.draw(win)
    return shape1, shape2, shape3
################################################################################
def randomObject():
    objList = ["square", "Tshape", "pole", "Rknight", "Lknight", "Rhorse",
               "Lhorse"]
    obj = objList[randrange(0, 7)]

    return obj
###############################################################################
#this creates the data for each square on the grid
    # each datum is a square in the grid. An example square key is 'grid[0.65][2.15]'
    #this would give ['a1', Point(2.15,0.65), False, 'black']
    # 'a1' represents row 'a' and column '1' and is the graphics object. the list is
    # [square object, center point, active, color]
def Data(win):
    grid = {}
    x,y = 2.15, 0.65
    alphabet = "abcdefghijklmnopqrstuv"
    for letter in alphabet:
        grid[y] = {}
        for column in range(1,11):
            grid[y][x] = [makeSquare(win,x,y), Point(round(x,2),round(y,2)), False, "black"]
            x = round(x + 0.3,2)
        x = 2.15
        y = round(y + 0.3,2)
    return grid
###############################################################################
def makeSquare(win,x,y):
    #this function makes the little squares in Data()
    x1 = round(x - 0.15, 2)
    y1 = round(y - 0.15, 2)
    x2 = round(x + 0.15, 2)
    y2 = round(y + 0.15, 2)
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    square = Rectangle(p1, p2)
    return square
    
    

#####################################################################################################        
def objGen(newObject, win, grid, pauseButton, quitButton, n):
    #objGen handles the creation and movement of the object (obj)
    if newObject == "square":
        obj = Square(win)
    elif newObject == "pole":
        obj = Pole(win)
    elif newObject == "Tshape":
        obj = Tshape(win)
    elif newObject == "Rknight":
        obj = Rknight(win)
    elif newObject == "Lknight":
        obj = Lknight(win)
    elif newObject == "Rhorse":
        obj = Rhorse(win)
    elif newObject == "Lhorse":
        obj = Lhorse(win)
        
    dKey = "Down"
    pause = False
    
    while True:
        pt = win.checkMouse()
        if type(pt) == Point:
            if pauseButton.clicked(pt):
                mixer.music.pause()
                pauseButton.setFill('red')
                while True:
                    pt2 = win.getMouse()
                    if type(pt2) == Point:
                        if pauseButton.clicked(pt2):
                            mixer.music.unpause()
                            pauseButton.setFill('green')
                            break
                        elif quitButton.clicked(pt2):
                            win.close()
                            import sys
                            mixer.music.stop()
                            sys.exit()
                            
            elif quitButton.clicked(pt):
                win.close()
                import sys
                mixer.music.stop()
                sys.exit()
                
        for i in range(10):
            keyStr = win.checkKey()
            if keyStr != "":
                if keyStr == "Left" and leftUnobstructed(obj, grid):
                    obj.move(keyStr)
                elif keyStr == "Right" and rightUnobstructed(obj, grid):
                    obj.move(keyStr)
                elif keyStr == "Down" and bottomUnobstructed(obj, grid):
                    obj.move(keyStr)
                elif keyStr == "space" and obj.type() != "square":
                    rotate(obj,grid, win)
                    winsound.PlaySound("click_x.wav",winsound.SND_ASYNC)
            update(n)
        if (obj.bottomEdge() <= 0.51) or (bottomUnobstructed(obj, grid) == False):
            changeGrid(obj, grid, win)
            # this line below can be deleted in order for the squares to stay seen
            obj.undraw()
            
            break
        
        obj.move(dKey)
        update(35)
        
    consecRows = HandleCompRows(grid, win)
    return consecRows
#####################################################################################################    
def HandleCompRows(grid, win):
    
    # HandleCompRows takes care of completed rows
    status, rowNum, row = completedRows(grid)
    consecRows = 0
    if rowNum != "":
        consecRows = 1
        origRowNum = rowNum
    while status:
        column = 2.15
        redClones = []
        for i in range(10):

            grid[row][column][0].setFill("red")
            # these 5 lines govern the squares shooting away
            redClones.append(grid[row][column][0].clone().draw(win))   
            grid[row][column][0].undraw() #here is where you'd put the row destruction animation
            grid[row][column][2] = False
            grid[row][column][3] = "black"
            column = round(column + 0.3, 2)
        winsound.PlaySound("gunshots2_x",winsound.SND_ASYNC)
        for i in redClones:
            rx = random() - 0.5
            ry = random() - 0.5
            for j in range(10):
                i.move(rx,ry)
                update(100)
            i.undraw()
        
        shiftDown(grid, win, rowNum, row)
        #redrawGrid(win)   <-------------------Activate this if you need to redraw the grid
                                                
        status, rowNum, row = completedRows(grid)
        if rowNum == origRowNum:
            consecRows = consecRows + 1
    return consecRows
##################################################################################################
def completedRows(grid):
    #this function determines if there are any completed rows
    x = 2.15
    y = 0.65
    rowCount = 0
    for row in range(20):
        for column in range(10):
            if grid[y][x][2] == True:
                rowCount = rowCount + 1
            x = round(x + 0.30, 2)
        if rowCount == 10:
            return True, row + 1, y
        rowCount = 0
        x = 2.15
        y = round(y + 0.30, 2)
    return False, "", ""

###################################################################################################

def shiftDown(grid, win, rowNum, ypos):
    # this shifts all the little squares down after a row deletion
    rowNum = rowNum + 1 # the initial rowNum and  ypos is the deleted 
    ypos = round(ypos + 0.30, 2)     # row so, add one to get the start row.

    x = 2.15
    n = 20 - rowNum + 1 # amount of times to run loop
    clones = [] # this is a list that will be cycled through
                # to animate squares moving down
    for row in range(n):
        for col in range(10):
            newypos = round(ypos - 0.30, 2)
            if grid[ypos][x][2] == True:    #change new space to True if old space is true
                grid[newypos][x][2] = True
                clones.append(grid[ypos][x][0].clone().draw(win)) # add each square's clone to the clones list
            grid[ypos][x][0].undraw()   # undraw the orig square
            grid[ypos][x][2] = False    # deactivate the orig square
            grid[newypos][x][3] = grid[ypos][x][3]  # change new space to color of old space
            grid[ypos][x][3] = "black"  # make fill black
            x = round(x + 0.30, 2)
        x = 2.15
        ypos = round(ypos + 0.30, 2)

    # animate the clones falling
    for i in clones:
        i.move(0, -0.30)
        c = i.getCenter() # new center
        nx = round(c.getX(), 2)   # new x center
        ny = round(c.getY(), 2)   # new y center
        grid[ny][nx][0] = i
        update(150)
#######################################################################################################
def rotate(obj, grid, win):
    state = obj.orientation()
    if obj.type() == "pole":
        if state == "layUp":
            stateList = ["standRight", "layDown", "standLeft"]
        elif state == "standRight":
            stateList = ["layDown", "standLeft", "layUp"]
        elif state == "layDown":
            stateList = ["standLeft", "layUp", "standRight"]
        elif state == "standLeft":
            stateList = ["layUp", "standRight", "layDown"]
    elif (obj.type() == "Tshape" or obj.type() == "Rknight" or
          obj.type() == "Lknight" or obj.type() == "Rhorse" or
          obj.type() == "Lhorse"):
        if state == "up":
            stateList = ["right", "down", "left"]
        elif state == "right":
            stateList = ["down", "left", "up"]
        elif state == "down":
            stateList = ["left", "up", "right"]
        elif state == "left":
            stateList = ["up", "right", "down"]
            
    for i in stateList:
        c1, c2, c3, c4 = obj.activeSquares(i)
        x1, x2, x3, x4 = round(c1.getX(),2), round(c2.getX(),2), round(c3.getX(),2), round(c4.getX(),2)
        y1, y2, y3, y4 = round(c1.getY(),2), round(c2.getY(),2), round(c3.getY(),2), round(c4.getY(),2)
        
        try:
            if ((grid[y1][x1][2] == False) and (grid[y2][x2][2] == False) and (grid[y3][x3][2] == False)
                and (grid[y4][x4][2] == False)):
                setState(obj, grid, win, i)
                break
            else:
                pass
                
        except KeyError:# as x:
##                if KeyError == 0.35 or KeyError == 7.25:
##                    print("no")
            #print("no")
            pass
        
    
########################################################################################################    
def setState(obj, grid, win, state):
    if obj.type() == "pole":
        if state == "layUp":
            obj.setlayUp(win)
        elif state == "standRight":
            obj.setstandRight(win)
        elif state == "layDown":
            obj.setlayDown(win)
        elif state == "standLeft":
            obj.setstandLeft(win)
    elif (obj.type() == "Tshape" or obj.type() == "Rknight" or
          obj.type() == "Lknight" or obj.type() == "Rhorse" or
          obj.type() == "Lhorse"):
        if state == "up":
            obj.setup(win)
        elif state == "right":
            obj.setright(win)
        elif state == "down":
            obj.setdown(win)
        elif state == "left":
            obj.setleft(win)
            
#########################################################################################################
###  changeGrid()
        
def changeGrid(obj, grid, win):
    if obj.type() == "square":
        c = obj.Center()
        cx = c.getX()
        cy = c.getY()
        LLx = ULx = round(cx - 0.15, 2)
        URy = ULy = round(cy + 0.15, 2)
        URx = LRx = round(cx + 0.15, 2)
        LLy = LRy = round(cy - 0.15, 2)
        #change 'activated'
        grid[ULy][ULx][2] = True
        grid[LLy][LLx][2] = True
        grid[URy][URx][2] = True
        grid[LRy][LRx][2] = True
        #change color
        grid[ULy][ULx][3] = str(obj.getFill())
        grid[LLy][LLx][3] = str(obj.getFill())
        grid[URy][URx][3] = str(obj.getFill())
        grid[LRy][LRx][3] = str(obj.getFill())
        # set squares' color
        grid[ULy][ULx][0].setFill(grid[ULy][ULx][3])
        grid[LLy][LLx][0].setFill(grid[LLy][LLx][3])
        grid[URy][URx][0].setFill(grid[URy][URx][3])
        grid[LRy][LRx][0].setFill(grid[LRy][LRx][3])
        #set squares' outline
        grid[ULy][ULx][0].setOutline(color_rgb(25,25,25))
        grid[LLy][LLx][0].setOutline(color_rgb(25,25,25))
        grid[URy][URx][0].setOutline(color_rgb(25,25,25))
        grid[LRy][LRx][0].setOutline(color_rgb(25,25,25))
        # set squares' width
        grid[ULy][ULx][0].setWidth(2)
        grid[LLy][LLx][0].setWidth(2)
        grid[URy][URx][0].setWidth(2)
        grid[LRy][LRx][0].setWidth(2)       
        # draw new squares
        grid[ULy][ULx][0].draw(win)
        grid[LLy][LLx][0].draw(win)
        grid[URy][URx][0].draw(win)
        grid[LRy][LRx][0].draw(win)
        


    elif (obj.type() == "pole" or obj.type() == "Tshape" or obj.type() == "Lhorse" or obj.type() == "Rhorse" or
          obj.type() == "Rknight" or obj.type() == "Lknight"):
        s1, s2, s3, s4 = obj.activeSquares(obj.orientation())
        x1, x2, x3, x4 = round(s1.getX(), 2), round(s2.getX(), 2), round(s3.getX(), 2), round(s4.getX(), 2)
        y1, y2, y3, y4 = round(s1.getY(), 2), round(s2.getY(), 2), round(s3.getY(), 2), round(s4.getY(), 2)
        
        # change 'activated'
        grid[y1][x1][2] = True
        grid[y2][x2][2] = True
        grid[y3][x3][2] = True
        grid[y4][x4][2] = True
        # change color
        grid[y1][x1][3] = str(obj.getFill())
        grid[y2][x2][3] = str(obj.getFill())
        grid[y3][x3][3] = str(obj.getFill())
        grid[y4][x4][3] = str(obj.getFill())
        # set squares' color
        grid[y1][x1][0].setFill(grid[y1][x1][3])
        grid[y2][x2][0].setFill(grid[y2][x2][3])
        grid[y3][x3][0].setFill(grid[y3][x3][3])
        grid[y4][x4][0].setFill(grid[y4][x4][3])
        # set squares' outline
        grid[y1][x1][0].setOutline(color_rgb(25,25,25))
        grid[y2][x2][0].setOutline(color_rgb(25,25,25))
        grid[y3][x3][0].setOutline(color_rgb(25,25,25))
        grid[y4][x4][0].setOutline(color_rgb(25,25,25))
        # set squares' width
        grid[y1][x1][0].setWidth(2)
        grid[y2][x2][0].setWidth(2)
        grid[y3][x3][0].setWidth(2)
        grid[y4][x4][0].setWidth(2)
        # draw new squares
        grid[y1][x1][0].draw(win)
        grid[y2][x2][0].draw(win)
        grid[y3][x3][0].draw(win)
        grid[y4][x4][0].draw(win)

    
    
###################################################################################################
        
def leftUnobstructed(obj, grid):
    #this function checks if an object would have it's leftwards movement obstructed
    #### square
    if obj.type() == "square":
        c = obj.Center()
        x = c.getX()
        y = c.getY()
        uL = Point(x - 0.15, y + 0.15)
        LL = Point(x - 0.15, y - 0.15)
        #(ux,uy) is the center of the space to the upper-left where the object may be
        # obstructed
        ux = round(uL.getX() - 0.3, 2)
        uy = round(uL.getY(), 2)
        #(Lx,Ly) is the center of the space to the lower-left where the object may be
        # obstructed        
        Lx = round(LL.getX() - 0.3, 2)
        Ly = round(LL.getY(), 2)
        try:
            if (grid[uy][ux][2] == False) and (grid[Ly][Lx][2] == False) and (obj.leftEdge() > 2.1):
                return True
            else:
                return False
        except KeyError as farLeft:
            if farLeft == 1.85:
                return False
    #### pole
    elif obj.type() == "pole":
        if obj.orientation() == "layUp" or obj.orientation() == "layDown":
            if obj.orientation() == "layUp":
                LL, ML, MR, RR = obj.activeSquares("layUp")
            elif obj.orientation() == "layDown":
                LL, ML, MR, RR = obj.activeSquares("layDown")
            try:
                if (grid[round(LL.getY(), 2)][round(LL.getX() - 0.30, 2)][2] == False) and (obj.leftEdge() > 2.1):
                    return True
                else:
                    return False
            except KeyError as farLeft:
                    if farLeft == 1.85:
                        return False
        elif obj.orientation() == "standRight" or obj.orientation() == "standLeft":
            if obj.orientation() == "standRight":
                UU, MU, ML, LL = obj.activeSquares("standRight")
            elif obj.orientation() == "standLeft":
                UU, MU, ML, LL = obj.activeSquares("standLeft")
            x = round(UU.getX() - 0.30, 2)
            y1, y2, y3, y4 = round(UU.getY(), 2), round(MU.getY(), 2), round(ML.getY(), 2), round(LL.getY(), 2)
            try:
                if ((grid[y1][x][2] == False) and (grid[y2][x][2] == False) and (grid[y3][x][2] == False) and
                    (grid[y4][x][2] == False) and (obj.leftEdge() > 2.1)):
                    return True
                else:
                    return False
            except KeyError as farLeft:
                    if farLeft == 1.85:
                        return False
### remaining shapes
    elif (obj.type() == "Tshape" or obj.type() == "Lhorse" or obj.type() == "Rhorse" or
          obj.type() == "Rknight" or obj.type() == "Lknight"):
        s1, s2, s3, s4 = obj.activeSquares(obj.orientation())
        x1, x2, x3, x4 = round(s1.getX() - 0.30, 2), round(s2.getX() - 0.30, 2), round(s3.getX() - 0.30, 2), round(s4.getX() - 0.30, 2)
        y1, y2, y3, y4 = round(s1.getY(), 2), round(s2.getY(), 2), round(s3.getY(), 2), round(s4.getY(), 2)
        try:
            if ((grid[y1][x1][2] == False) and (grid[y2][x2][2] == False) and (grid[y3][x3][2] == False) and
                (grid[y4][x4][2] == False) and (obj.leftEdge() > 2.1)):
                return True
            else:
                return False
        except KeyError as farLeft:
                if farLeft == 1.85:
                    return False    
         
###############################################################################################################

def rightUnobstructed(obj, grid):
    # this function checks if an object would have it's rightwards movement obstructed
    if obj.type() == "square":
        c = obj.Center()
        cx = c.getX()
        cy = c.getY()
        Fx = round(cx + 0.45, 2)
        FUy = round(cy + 0.15, 2)
        FLy = round(cy - 0.15, 2)
        try:
            if (grid[FUy][Fx][2] == False) and (grid[FLy][Fx][2] == False) and obj.rightEdge() < 4.9:
                return True
            else:
                return False
        except KeyError as farRight:
            if farRight == 5.15:
                return False
    #### pole
    elif obj.type() == "pole":
        if obj.orientation() == "layUp" or obj.orientation() == "layDown":
            if obj.orientation() == "layUp":
                LL, ML, MR, RR = obj.activeSquares("layUp")
            elif obj.orientation() == "layDown":
                LL, ML, MR, RR = obj.activeSquares("layDown")
            try:
                if (grid[round(RR.getY(), 2)][round(RR.getX() + 0.30, 2)][2] == False) and (obj.rightEdge() < 4.9):
                    return True
                else:
                    return False
            except KeyError as farRight:
                if farRight == 5.15:
                    return False
        elif obj.orientation() == "standRight" or obj.orientation() == "standLeft":
            if obj.orientation() == "standRight":
                UU, MU, ML, LL = obj.activeSquares("standRight")
            elif obj.orientation() == "standLeft":
                UU, MU, ML, LL = obj.activeSquares("standLeft")
            x = round(UU.getX() + 0.30, 2)
            y1, y2, y3, y4 = round(UU.getY(), 2), round(MU.getY(), 2), round(ML.getY(), 2), round(LL.getY(), 2)
            try:
                if ((grid[y1][x][2] == False) and (grid[y2][x][2] == False) and (grid[y3][x][2] == False) and
                    (grid[y4][x][2] == False) and (obj.rightEdge() < 4.9)):
                    return True
                else:
                    return False
            except KeyError as farRight:
                    if farRight == 5.15:
                        return False

# remaining shapes
    elif (obj.type() == "Tshape" or obj.type() == "Lhorse" or obj.type() == "Rhorse" or
          obj.type() == "Rknight" or obj.type() == "Lknight"):
        s1, s2, s3, s4 = obj.activeSquares(obj.orientation())
        x1, x2, x3, x4 = round(s1.getX() + 0.30, 2), round(s2.getX() + 0.30, 2), round(s3.getX() + 0.30, 2), round(s4.getX() + 0.30, 2)
        y1, y2, y3, y4 = round(s1.getY(), 2), round(s2.getY(), 2), round(s3.getY(), 2), round(s4.getY(), 2)
        try:
            if ((grid[y1][x1][2] == False) and (grid[y2][x2][2] == False) and (grid[y3][x3][2] == False) and
                (grid[y4][x4][2] == False) and (obj.rightEdge() < 4.9)):
                return True
            else:
                return False
        except KeyError as farRight:
                if farRight == 5.15:
                    return False  
                    
#####################################################################################################                                                                                         

def bottomUnobstructed(obj, grid):
    #this function checks if an object would have its downward movement obstructed
    if obj.type() == "square":
        c = obj.Center()
        cx = c.getX()
        cy = c.getY()
        FLx = round(cx - 0.15, 2)
        Fy = round(cy - 0.45, 2)
        FRx = round(cx + 0.15, 2)
        try:
            if (grid[Fy][FLx][2] == False) and (grid[Fy][FRx][2] == False) and (obj.bottomEdge() > 0.51):
                return True
            else:
                return False
        except KeyError as bottom:
            if bottom == 0.35:
                return False
    #### pole
    elif obj.type() == "pole":
        if obj.orientation() == "layUp" or obj.orientation() == "layDown":
            if obj.orientation() == "layUp":
                LL, ML, MR, RR = obj.activeSquares("layUp")
            elif obj.orientation() == "layDown":
                LL, ML, MR, RR = obj.activeSquares("layDown")
                    
            y = round(LL.getY() - 0.30, 2)
            x1, x2, x3, x4 = round(LL.getX(),2), round(ML.getX(),2), round(MR.getX(),2), round(RR.getX(),2)
            try:
                if ((grid[y][x1][2] == False) and (grid[y][x2][2] == False) and 
                (grid[y][x3][2] == False) and (grid[y][x4][2] == False) and (obj.bottomEdge() > 0.51)):
                    return True
                else:
                    return False
            except KeyError as bottom:
                if bottom == 0.35:
                    return False
        elif obj.orientation() == "standRight" or obj.orientation() == "standLeft":
            if obj.orientation() == "standRight":
                UU, MU, ML, LL = obj.activeSquares("standRight")
            elif obj.orientation() == "standLeft":
                UU, MU, ML, LL = obj.activeSquares("standLeft")
            y = round(LL.getY() - 0.30, 2)
            x = round(LL.getX(), 2)
            try:
                if (grid[y][x][2] == False) and (obj.bottomEdge() > 0.51):
                    return True
                else:
                    return False
            except KeyError as bottom:
                if bottom == 0.35:
                    return False

### remaining shape objects
    elif (obj.type() == "Tshape" or obj.type() == "Lhorse" or obj.type() == "Rhorse" or
          obj.type() == "Rknight" or obj.type() == "Lknight"):
        s1, s2, s3, s4 = obj.activeSquares(obj.orientation())
        x1, x2, x3, x4 = round(s1.getX(), 2), round(s2.getX(), 2), round(s3.getX(), 2), round(s4.getX(), 2)
        y1, y2, y3, y4 = round(s1.getY() - 0.30, 2), round(s2.getY() - 0.30, 2), round(s3.getY() - 0.30, 2), round(s4.getY() - 0.30, 2)
        try:
            if ((grid[y1][x1][2] == False) and (grid[y2][x2][2] == False) and (grid[y3][x3][2] == False) and
                (grid[y4][x4][2] == False) and (obj.bottomEdge() > 0.51)):
                return True
            else:
                return False
        except KeyError as bottom:
                if bottom == 0.35:
                    return False 
                
                
                
#####################################################################################################
         
def redrawGrid(win):
        #make gridlines
    color = color_rgb(25,25,25)
    #make vertical lines
    x = 2.3
    y = 0.5
    yH = 6.5
    for i in range(9):
        l = Line(Point(x,y), Point(x,yH))
        l.setFill(color)
        l.draw(win)
        x = x + 0.3

    #make horizontal lines
    x = 2.0
    xL = 5.0
    y = 0.8
    for i in range(19):
        l = Line(Point(x,y), Point(xL,y))
        l.setFill(color)
        l.draw(win)
        y = y + 0.3

def makeGrid():
    win = GraphWin("Not Tetris", 700, 800, autoflush = False)
    win.setCoords(0.0, 0.0, 7.0, 8.0)
    win.setBackground("silver")
    
    #create background
    rec = Rectangle(Point(2.0, 0.5), Point(5.0, 6.5))
    rec.setFill("black")
    rec.setOutline("blue")
    rec.setWidth(2)
    rec.draw(win)

    # create preview box
    rec2 = Rectangle(Point(5.5, 5.5), Point(6.5, 6.8)).draw(win)
    rec2.setFill("black")

    #make gridlines
    color = color_rgb(25,25,25)
    #make vertical lines
    x = 2.3
    y = 0.5
    yH = 6.5
    for i in range(9):
        l = Line(Point(x,y), Point(x,yH))
        l.setFill(color)
        l.setWidth(2)
        l.draw(win)
        x = x + 0.3

    #make horizontal lines
    x = 2.0
    xL = 5.0
    y = 0.8
    for i in range(19):
        l = Line(Point(x,y), Point(xL,y))
        l.setFill(color)
        l.setWidth(2)
        l.draw(win)
        y = y + 0.3
    return win
    
if __name__ == "__main__": main()
