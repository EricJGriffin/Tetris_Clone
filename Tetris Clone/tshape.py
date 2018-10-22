# tshape.py
# a tetris T-shape object
from graphics import *

class Tshape:
    """ This class initializes a Tshape object using setCoords."""

    def __init__(self, window):
        # there are 4 orientations/states: 'up', 'right', 'left', and
        # 'down'. 4 separate objects.
        p1 = Point(3.50, 7.10)
        p2 = Point(3.80, 6.80)
        p3 = Point(3.20, 6.80)
        p4 = Point(3.80, 7.40)
        p5 = Point(3.50, 6.50)
        p6 = Point(4.10, 7.10)

        self.fill = "purple"
        ## create square outlines
        self.sqC = Rectangle(p1, p2).draw(window) # center square
        self.sqT = Rectangle(p1, p4)              # top square
        self.sqR = Rectangle(p2, p6).draw(window) # right square
        self.sqB = Rectangle(p5, p2).draw(window) # bottom square
        self.sqL = Rectangle(p3, p1).draw(window) # left square
        ## set square fills and square outline colors
        self.sqC.setFill(self.fill)
        self.sqT.setFill(self.fill)
        self.sqR.setFill(self.fill)
        self.sqB.setFill(self.fill)
        self.sqL.setFill(self.fill)

        self.sqC.setOutline(color_rgb(25,25,25))
        self.sqT.setOutline(color_rgb(25,25,25))
        self.sqR.setOutline(color_rgb(25,25,25))
        self.sqB.setOutline(color_rgb(25,25,25))
        self.sqL.setOutline(color_rgb(25,25,25))

        #set width
        self.sqC.setWidth(2)
        self.sqT.setWidth(2)
        self.sqR.setWidth(2)
        self.sqB.setWidth(2)
        self.sqL.setWidth(2)

        self.activeState = "down" # the method to represent this is .orientation()
###############################################################################
    # this formula moves the object in the directions: 'Down', 'Left' and 'Right'
    def move(self, key):
        if key == "Right":
            self.sqC.move(0.30, 0.0)
            self.sqT.move(0.30, 0.0)
            self.sqR.move(0.30, 0.0)
            self.sqB.move(0.30, 0.0)
            self.sqL.move(0.30, 0.0)

        if key == "Left":
            self.sqC.move(-0.30, 0.0)
            self.sqT.move(-0.30, 0.0)
            self.sqR.move(-0.30, 0.0)
            self.sqB.move(-0.30, 0.0)
            self.sqL.move(-0.30, 0.0)           

        if key == "Down":
            self.sqC.move(0.0, -0.30)
            self.sqT.move(0.0, -0.30)
            self.sqR.move(0.0, -0.30)
            self.sqB.move(0.0, -0.30)
            self.sqL.move(0.0, -0.30)
        
#############################################################################
    # this section (the next 4 formulas) covers the rotations
    def setright(self, window):
        if self.activeState == "down":
            self.sqL.undraw()
            self.sqT.draw(window)
        elif self.activeState == "left":
            self.sqL.undraw()
            self.sqR.draw(window)
        elif self.activeState == "up":
            self.sqL.undraw()
            self.sqB.draw(window)
        self.activeState = "right"

    def setup(self, window):
        if self.activeState == "right":
            self.sqB.undraw()
            self.sqL.draw(window)
        elif self.activeState == "down":
            self.sqB.undraw()
            self.sqT.draw(window)
        elif self.activeState == "left":
            self.sqB.undraw()
            self.sqR.draw(window)
        self.activeState = "up"

    def setdown(self, window):
        if self.activeState == "up":
            self.sqT.undraw()
            self.sqB.draw(window)
        elif self.activeState == "right":
            self.sqT.undraw()
            self.sqL.draw(window)
        elif self.activeState == "left":
            self.sqT.undraw()
            self.sqR.draw(window)
        self.activeState = "down"

    def setleft(self, window):
        if self.activeState == "up":
            self.sqR.undraw()
            self.sqB.draw(window)
        elif self.activeState == "right":
            self.sqR.undraw()
            self.sqL.draw(window)
        elif self.activeState == "down":
            self.sqR.undraw()
            self.sqT.draw(window)
        self.activeState = "left"
    
##########################################################################
    
## this method indicates which square centers are active for a given state
    def activeSquares(self, state):
        if state == "up":
            top = self.sqT.getCenter()
            left = self.sqL.getCenter()
            center = self.sqC.getCenter()
            right = self.sqR.getCenter()
            return center, left, top, right
        elif state == "right":
            center = self.sqC.getCenter()
            top = self.sqT.getCenter()
            right = self.sqR.getCenter()
            bottom = self.sqB.getCenter()
            return center, top, right, bottom
        elif state == "down":
            center = self.sqC.getCenter()
            right = self.sqR.getCenter()
            bottom = self.sqB.getCenter()
            left = self.sqL.getCenter()
            return center, right, bottom, left
        elif state == "left":
            center = self.sqC.getCenter()
            top = self.sqT.getCenter()
            left = self.sqL.getCenter()
            bottom = self.sqB.getCenter()
            return center, top, left, bottom
###########################################################################
    def bottomEdge(self):
        if self.activeState == "up":
            return round(self.sqC.getCenter().getY() - 0.15, 2)
        elif (self.activeState == "right" or self.activeState == "left" or
              self.activeState == "down"):
            return round(self.sqB.getCenter().getY() - 0.15, 2)

    def leftEdge(self):
        if (self.activeState == "up" or self.activeState == "left" or
            self.activeState == "down"):
            return round(self.sqL.getCenter().getX() - 0.15, 2)
        elif self.activeState == "right":
            return round(self.sqC.getCenter().getX() - 0.15, 2)

    def rightEdge(self):
        if (self.activeState == "up" or self.activeState == "right" or
            self.activeState == "down"):
            return round(self.sqR.getCenter().getX() - 0.15, 2)
        elif self.activeState == "left":
            return round(self.sqC.getCenter().getX() - 0.15, 2)

    def Center(self):
        return self.sqC.getCenter()

    def getFill(self):
        return self.fill

    def undraw(self):
        self.sqC.undraw()
        self.sqL.undraw()
        self.sqR.undraw()
        self.sqT.undraw()
        self.sqB.undraw()

    def type(self):
        return "Tshape"

    def orientation(self):
        return self.activeState
