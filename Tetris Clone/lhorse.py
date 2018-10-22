# lhorse.py
# a tetris Lhorse shape object
from graphics import *

class Lhorse:
    """This class initializes a Lhorse object using setCoords."""
    def __init__(self, window):
        # there are 4 orientations/states : 'up', 'right', down' and
        # 'left'. the direction refers to the appearance of a horse
        # facing to the left in positions 'up' and 'down'
        p1 = Point(3.20, 7.40)
        p2 = Point(3.50, 7.10)
        p3 = Point(3.20, 6.80)
        p4 = Point(3.80, 6.80)
        p5 = Point(4.10, 7.10)
        p6 = Point(3.80, 7.40)
        p7 = Point(3.50, 6.50)
        p8 = Point(4.10, 6.50)

        self.fill = "red"
        #create squares' outlines
        self.TL = Rectangle(p1, p2).draw(window) # Top Left
        self.TM = Rectangle(p2, p6).draw(window) # Top Middle
        self.TR = Rectangle(p6, p5)              # Top Right
        self.ML = Rectangle(p3, p2)              # Middle Left
        self.MM = Rectangle(p2, p4).draw(window) # Middle Middle
        self.MR = Rectangle(p4, p5).draw(window) # Middle Right
        self.BL = Rectangle(p3, p7)              # Bottom Left
        self.BM = Rectangle(p7, p4)              # Bottom Middle
        self.BR = Rectangle(p4, p8)              # Bottom Right
        ## set square fills and square outline colors
        self.TL.setFill(self.fill)
        self.TM.setFill(self.fill)
        self.TR.setFill(self.fill)
        self.ML.setFill(self.fill)
        self.MM.setFill(self.fill)
        self.MR.setFill(self.fill)
        self.BL.setFill(self.fill)
        self.BM.setFill(self.fill)
        self.BR.setFill(self.fill)
        ## set square width
        self.TL.setWidth(2)
        self.TM.setWidth(2)
        self.TR.setWidth(2)
        self.ML.setWidth(2)
        self.MM.setWidth(2)
        self.MR.setWidth(2)
        self.BL.setWidth(2)
        self.BM.setWidth(2)
        self.BR.setWidth(2)
        
        self.TL.setOutline(color_rgb(25,25,25))
        self.TM.setOutline(color_rgb(25,25,25))
        self.TR.setOutline(color_rgb(25,25,25))
        self.ML.setOutline(color_rgb(25,25,25))
        self.MM.setOutline(color_rgb(25,25,25))
        self.MR.setOutline(color_rgb(25,25,25))
        self.BL.setOutline(color_rgb(25,25,25))
        self.BM.setOutline(color_rgb(25,25,25))
        self.BR.setOutline(color_rgb(25,25,25))

        self.activeState = "up" # the method to represent this is .orientation
##################################################################################
        # this formula moves the object in the directions: 'Down', 'Left' and 'Right'
    def move(self, key):
        if key == "Right":
            self.TL.move(0.30, 0.0)
            self.TM.move(0.30, 0.0)
            self.TR.move(0.30, 0.0)
            self.ML.move(0.30, 0.0)
            self.MM.move(0.30, 0.0)
            self.MR.move(0.30, 0.0)
            self.BL.move(0.30, 0.0)
            self.BM.move(0.30, 0.0)
            self.BR.move(0.30, 0.0)
        elif key == "Left":
            self.TL.move(-0.30, 0.0)
            self.TM.move(-0.30, 0.0)
            self.TR.move(-0.30, 0.0)
            self.ML.move(-0.30, 0.0)
            self.MM.move(-0.30, 0.0)
            self.MR.move(-0.30, 0.0)
            self.BL.move(-0.30, 0.0)
            self.BM.move(-0.30, 0.0)
            self.BR.move(-0.30, 0.0)
        elif key == "Down":
            self.TL.move(0.0, -0.30)
            self.TM.move(0.0, -0.30)
            self.TR.move(0.0, -0.30)
            self.ML.move(0.0, -0.30)
            self.MM.move(0.0, -0.30)
            self.MR.move(0.0, -0.30)
            self.BL.move(0.0, -0.30)
            self.BM.move(0.0, -0.30)
            self.BR.move(0.0, -0.30)
###############################################################################
    # this section ( the next 4 formulas) covers the rotations
    def setup(self, window):
        if self.activeState == "right":
            self.TR.undraw()
            self.BM.undraw()
            self.TM.draw(window)
            self.TL.draw(window)
        elif self.activeState == "down":
            self.ML.undraw()
            self.BM.undraw()
            self.BR.undraw()
            self.MR.draw(window)
            self.TM.draw(window)
            self.TL.draw(window)
        elif self.activeState == "left":
            self.ML.undraw()
            self.BL.undraw()
            self.MR.draw(window)
            self.TL.draw(window)
        self.activeState = "up"

    def setright(self, window):
        if self.activeState == "up":
            self.TM.undraw()
            self.TL.undraw()
            self.BM.draw(window)
            self.TR.draw(window)
        elif self.activeState == "down":
            self.BR.undraw()
            self.ML.undraw()
            self.TR.draw(window)
            self.MR.draw(window)
        elif self.activeState == "left":
            self.BL.undraw()
            self.ML.undraw()
            self.TM.undraw()
            self.BM.draw(window)
            self.MR.draw(window)
            self.TR.draw(window)
        self.activeState = "right"

    def setdown(self, window):
        if self.activeState == "up":
            self.TM.undraw()
            self.TL.undraw()
            self.MR.undraw()
            self.ML.draw(window)
            self.BM.draw(window)
            self.BR.draw(window)
        elif self.activeState == "right":
            self.TR.undraw()
            self.MR.undraw()
            self.BR.draw(window)
            self.ML.draw(window)
        elif self.activeState == "left":
            self.BL.undraw()
            self.TM.undraw()
            self.BM.draw(window)
            self.BR.draw(window)
        self.activeState = "down"

    def setleft(self, window):
        if self.activeState == "up":
            self.TL.undraw()
            self.MR.undraw()
            self.ML.draw(window)
            self.BL.draw(window)
        elif self.activeState == "right":
            self.TR.undraw()
            self.MR.undraw()
            self.BM.undraw()
            self.TM.draw(window)
            self.ML.draw(window)
            self.BL.draw(window)
        elif self.activeState == "down":
            self.BM.undraw()
            self.BR.undraw()
            self.BL.draw(window)
            self.TM.draw(window)
        self.activeState = "left"
            
##############################################################################
    ## this method indicates which square centers are active for a given state
    def activeSquares(self, state):
        if state == "up":
            TL = self.TL.getCenter()
            TM = self.TM.getCenter()
            MM = self.MM.getCenter()
            MR = self.MR.getCenter()
            return TL, TM, MM, MR
        elif state == "right":
            TR = self.TR.getCenter()
            MM = self.MM.getCenter()
            MR = self.MR.getCenter()
            BM = self.BM.getCenter()
            return TR, MM, MR, BM
        elif state == "down":
            MM = self.MM.getCenter()
            ML = self.ML.getCenter()
            BM = self.BM.getCenter()
            BR = self.BR.getCenter()
            return MM, ML, BM, BR
        elif state == "left":
            TM = self.TM.getCenter()
            ML = self.ML.getCenter()
            MM = self.MM.getCenter()
            BL = self.BL.getCenter()
            return TM, ML, MM, BL

################################################################################
    def bottomEdge(self):
        if self.activeState == "up":
            return round(self.MM.getCenter().getY() - 0.15, 2)
        elif (self.activeState == "right" or self.activeState == "left" or
              self.activeState == "down"):
            return round(self.BM.getCenter().getY() - 0.15, 2)

    def leftEdge(self):
        if self.activeState == "right":
            return round(self.MM.getCenter().getX() - 0.15, 2)
        elif (self.activeState == "left" or self.activeState == "up" or
              self.activeState == "down"):
            return round(self.ML.getCenter().getX() - 0.15, 2)

    def rightEdge(self):
        if self.activeState == "left":
            return round(self.MM.getCenter().getX() + 0.15, 2)
        elif (self.activeState == "right" or self.activeState == "up" or
              self.activeState == "down"):
            return round(self.MR.getCenter().getX() + 0.15, 2)

    def Center(self):
        return self.MM.getCenter()

    def getFill(self):
        return self.fill
    def undraw(self):
        self.TL.undraw()
        self.TM.undraw()
        self.TR.undraw()
        self.ML.undraw()
        self.MM.undraw()
        self.MR.undraw()
        self.BL.undraw()
        self.BM.undraw()
        self.BR.undraw()

    def type(self):
        return "Lhorse"

    def orientation(self):
        return self.activeState
    
