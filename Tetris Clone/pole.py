# pole.py
# a tetris pole object
from graphics import *

class Pole:
    """ This class initializes a Pole object using setCoords."""

    def __init__(self, window):
        # there are four separate orientations or 'states': layUp,
        # standRight, layDown, standLeft.
        # In this class, there will be 4 separate objects/rectangles
        # to represent each state. One object/state will be active
        # at any given time

        ## all the points involved in rectangle boundaries:
        p1 = Point(2.90, 6.80)
        p2 = Point(4.10, 7.10)
        p3 = Point(4.10, 6.50)
        p4 = Point(3.80, 7.40)
        p5 = Point(3.50, 6.20)
        p6 = Point(3.20, 7.40)

        ## all the points involved in rectangle inner lines:
        p7 = Point(3.20, 6.80)
        p8 = Point(3.50, 6.80)
        p9 = Point(3.80, 6.80)
        p10 = Point(3.20, 7.10)
        p11 = Point(3.50, 7.10)
        p12 = Point(3.80, 7.10)
        p13 = Point(3.20, 6.50)
        p14 = Point(3.50, 6.50)
        p15 = Point(3.80, 6.50)

        self.fill = "aqua"

        ## outline and inner lines for layUp:
        self.layUpRec = Rectangle(p1, p2).draw(window)
        self.layUpRec.setFill(self.fill)
        self.layUpRec.setOutline(color_rgb(25,25,25))
        self.layUpL1 = Line(p7, p10).draw(window)
        self.layUpL1.setFill(color_rgb(25,25,25))
        self.layUpL2 = Line(p8, p11).draw(window)
        self.layUpL2.setFill(color_rgb(25,25,25))
        self.layUpL3 = Line(p9, p12).draw(window)
        self.layUpL3.setFill(color_rgb(25,25,25))
        self.layUpRec.setWidth(2)
        self.layUpL1.setWidth(2)
        self.layUpL2.setWidth(2)
        self.layUpL3.setWidth(2)


        ## outline and inner lines for layDown:
        self.layDownRec = Rectangle(p1, p3)
        self.layDownRec.setFill(self.fill)
        self.layDownRec.setOutline(color_rgb(25,25,25))
        self.layDownL1 = Line(p7, p13)
        self.layDownL1.setFill(color_rgb(25,25,25))
        self.layDownL2 = Line(p8, p14)
        self.layDownL2.setFill(color_rgb(25,25,25))
        self.layDownL3 = Line(p9, p15)
        self.layDownL3.setFill(color_rgb(25,25,25))
        self.layDownRec.setWidth(2)
        self.layDownL1.setWidth(2)
        self.layDownL2.setWidth(2)
        self.layDownL3.setWidth(2)

        ## outline and inner lines for standRight:
        self.standRightRec = Rectangle(p5, p4)
        self.standRightRec.setFill(self.fill)
        self.standRightRec.setOutline(color_rgb(25,25,25))
        self.standRightL1 = Line(p14, p15)
        self.standRightL1.setFill(color_rgb(25,25,25))
        self.standRightL2 = Line(p8, p9)
        self.standRightL2.setFill(color_rgb(25,25,25))
        self.standRightL3 = Line(p11, p12)
        self.standRightL3.setFill(color_rgb(25,25,25))
        self.standRightRec.setWidth(2)
        self.standRightL1.setWidth(2)
        self.standRightL2.setWidth(2)
        self.standRightL3.setWidth(2)

        ## outline and inner lines for standLeft:
        self.standLeftRec = Rectangle(p5, p6)
        self.standLeftRec.setFill(self.fill)
        self.standLeftRec.setOutline(color_rgb(25,25,25))
        self.standLeftL1 = Line(p10, p11)
        self.standLeftL1.setFill(color_rgb(25,25,25))
        self.standLeftL2 = Line(p7, p8)
        self.standLeftL2.setFill(color_rgb(25,25,25))
        self.standLeftL3 = Line(p13, p14)
        self.standLeftL3.setFill(color_rgb(25,25,25))
        self.standLeftRec.setWidth(2)
        self.standLeftL1.setWidth(2)
        self.standLeftL2.setWidth(2)
        self.standLeftL3.setWidth(2)

        self.activeState = "layUp" # the method to represent this is .orientation()
####################################################################################
#This formula moves the object in a direction ie. 'Down', 'Left', 'Right'
    def move(self, key):
        if key == "Right":
            self.layUpRec.move(0.30, 0)
            self.layUpL1.move(0.3, 0)
            self.layUpL2.move(0.3, 0)
            self.layUpL3.move(0.3, 0)

            self.layDownRec.move(0.3, 0)
            self.layDownL1.move(0.3, 0)
            self.layDownL2.move(0.3, 0)
            self.layDownL3.move(0.3, 0)

            self.standRightRec.move(0.3, 0)
            self.standRightL1.move(0.3, 0)
            self.standRightL2.move(0.3, 0)
            self.standRightL3.move(0.3, 0)

            self.standLeftRec.move(0.3, 0)
            self.standLeftL1.move(0.3, 0)
            self.standLeftL2.move(0.3, 0)
            self.standLeftL3.move(0.3, 0)

        if key == "Left":
            self.layUpRec.move(-0.3, 0)
            self.layUpL1.move(-0.3, 0)
            self.layUpL2.move(-0.3, 0)
            self.layUpL3.move(-0.3, 0)

            self.layDownRec.move(-0.3, 0)
            self.layDownL1.move(-0.3, 0)
            self.layDownL2.move(-0.3, 0)
            self.layDownL3.move(-0.3, 0)

            self.standRightRec.move(-0.3, 0)
            self.standRightL1.move(-0.3, 0)
            self.standRightL2.move(-0.3, 0)
            self.standRightL3.move(-0.3, 0)

            self.standLeftRec.move(-0.3, 0)
            self.standLeftL1.move(-0.3, 0)
            self.standLeftL2.move(-0.3, 0)
            self.standLeftL3.move(-0.3, 0)

        if key == "Down":
            self.layUpRec.move(0, -0.3)
            self.layUpL1.move(0, -0.3)
            self.layUpL2.move(0, -0.3)
            self.layUpL3.move(0, -0.3)

            self.layDownRec.move(0, -0.3)
            self.layDownL1.move(0, -0.3)
            self.layDownL2.move(0, -0.3)
            self.layDownL3.move(0, -0.3)

            self.standRightRec.move(0, -0.3)
            self.standRightL1.move(0, -0.3)
            self.standRightL2.move(0, -0.3)
            self.standRightL3.move(0, -0.3)

            self.standLeftRec.move(0, -0.3)
            self.standLeftL1.move(0, -0.3)
            self.standLeftL2.move(0, -0.3)
            self.standLeftL3.move(0, -0.3)

#################################################################################
#This section(the next 4 formulas) covers the rotations

    def setstandRight(self, window):
        if self.activeState == "layUp":
            # undraw layUp
            self.layUpRec.undraw()
            self.layUpL1.undraw()
            self.layUpL2.undraw()
            self.layUpL3.undraw()
        elif self.activeState == "layDown":
            # undraw layDown            
            self.layDownRec.undraw()
            self.layDownL1.undraw()
            self.layDownL2.undraw()
            self.layDownL3.undraw()
        elif self.activeState == "standLeft":
            # undraw standLeft
            self.standLeftRec.undraw()
            self.standLeftL1.undraw()
            self.standLeftL2.undraw()
            self.standLeftL3.undraw()
            
        self.activeState = "standRight" # set activeState to 'standRight'
        # draw standRight
        self.standRightRec.draw(window)
        self.standRightL1.draw(window)
        self.standRightL2.draw(window)
        self.standRightL3.draw(window)

    def setlayUp(self, window):    
        if self.activeState == "standRight":
            # undraw standRight
            self.standRightRec.undraw()
            self.standRightL1.undraw()
            self.standRightL2.undraw()
            self.standRightL3.undraw()
        elif self.activeState == "layDown":
            # undraw layDown            
            self.layDownRec.undraw()
            self.layDownL1.undraw()
            self.layDownL2.undraw()
            self.layDownL3.undraw()
        elif self.activeState == "standLeft":
            # undraw standLeft
            self.standLeftRec.undraw()
            self.standLeftL1.undraw()
            self.standLeftL2.undraw()
            self.standLeftL3.undraw()

        self.activeState = "layUp" # set activeState to 'layUp'
        # draw layUp
        self.layUpRec.draw(window)
        self.layUpL1.draw(window)
        self.layUpL2.draw(window)
        self.layUpL3.draw(window)

    def setlayDown(self, window):
        if self.activeState == "standRight":
            # undraw standRight
            self.standRightRec.undraw()
            self.standRightL1.undraw()
            self.standRightL2.undraw()
            self.standRightL3.undraw()
        elif self.activeState == "standLeft":
            # undraw standLeft
            self.standLeftRec.undraw()
            self.standLeftL1.undraw()
            self.standLeftL2.undraw()
            self.standLeftL3.undraw()
        elif self.activeState == "layUp":
            # undraw layUp
            self.layUpRec.undraw()
            self.layUpL1.undraw()
            self.layUpL2.undraw()
            self.layUpL3.undraw()

        self.activeState = "layDown" # set activeState to 'layDown'
        # draw layDown
        self.layDownRec.draw(window)
        self.layDownL1.draw(window)
        self.layDownL2.draw(window)
        self.layDownL3.draw(window)

    def setstandLeft(self, window):
        if self.activeState == "standRight":
            # undraw standRight
            self.standRightRec.undraw()
            self.standRightL1.undraw()
            self.standRightL2.undraw()
            self.standRightL3.undraw()
        elif self.activeState == "layUp":
            # undraw layUp
            self.layUpRec.undraw()
            self.layUpL1.undraw()
            self.layUpL2.undraw()
            self.layUpL3.undraw()
        elif self.activeState == "layDown":
            # undraw layDown            
            self.layDownRec.undraw()
            self.layDownL1.undraw()
            self.layDownL2.undraw()
            self.layDownL3.undraw()
        
        self.activeState = "standLeft" # set activeState to 'standLeft'
        # draw standLeft
        self.standLeftRec.draw(window)
        self.standLeftL1.draw(window)
        self.standLeftL2.draw(window)
        self.standLeftL3.draw(window)
###################################################################################

    #this method indicates which square centers are active for a given state
    def activeSquares(self, state):
        
        if state == "layUp":
            layUpCent = self.layUpRec.getCenter()
            LL = Point(round(layUpCent.getX(),2) - round(0.45, 2), round(layUpCent.getY(),2)) # far left square center
            ML = Point(round(layUpCent.getX(),2) - round(0.15, 2), round(layUpCent.getY(),2)) # middle left square center
            MR = Point(round(layUpCent.getX(),2) + round(0.15, 2), round(layUpCent.getY(),2)) # middle right square center
            RR = Point(round(layUpCent.getX(),2) + round(0.45, 2), round(layUpCent.getY(),2)) # far right square center
            return LL, ML, MR, RR
        elif state == "layDown":
            layDownCent = self.layDownRec.getCenter()
            LL = Point(round(layDownCent.getX(),2) - round(0.45, 2), round(layDownCent.getY(),2)) # far left square center
            ML = Point(round(layDownCent.getX(),2) - round(0.15, 2), round(layDownCent.getY(),2)) # middle left square center
            MR = Point(round(layDownCent.getX(),2) + round(0.15, 2), round(layDownCent.getY(),2)) # middle right square center
            RR = Point(round(layDownCent.getX(),2) + round(0.45, 2), round(layDownCent.getY(),2)) # far right square center
            return LL, ML, MR, RR            
        elif state == "standRight":
            standRightCent = self.standRightRec.getCenter()
            UU = Point(round(standRightCent.getX(),2), round(standRightCent.getY(),2) + round(0.45, 2)) # upper most square center
            MU = Point(round(standRightCent.getX(),2), round(standRightCent.getY(),2) + round(0.15, 2)) # middle upper square center
            ML = Point(round(standRightCent.getX(),2), round(standRightCent.getY(),2) - round(0.15, 2)) # middle lower square center
            LL = Point(round(standRightCent.getX(),2), round(standRightCent.getY(),2) - round(0.45, 2)) # lower most square center
            return UU, MU, ML, LL
        elif state == "standLeft":
            standLeftCent = self.standLeftRec.getCenter()
            UU = Point(round(standLeftCent.getX(),2), round(standLeftCent.getY(),2) + round(0.45, 2)) # upper most square center
            MU = Point(round(standLeftCent.getX(),2), round(standLeftCent.getY(),2) + round(0.15, 2)) # middle upper square center
            ML = Point(round(standLeftCent.getX(),2), round(standLeftCent.getY(),2) - round(0.15, 2)) # middle lower square center
            LL = Point(round(standLeftCent.getX(),2), round(standLeftCent.getY(),2) - round(0.45, 2)) # lower most square center
            return UU, MU, ML, LL

    def bottomEdge(self):
        if self.activeState == "layUp":
            return self.layUpRec.getCenter().getY() - round(0.15, 2)
        elif self.activeState == "layDown":
            return self.layDownRec.getCenter().getY() - round(0.15, 2)
        elif self.activeState == "standRight":
            return self.standRightRec.getCenter().getY() - round(0.60, 2)
        elif self.activeState == "standLeft":
            return self.standLeftRec.getCenter().getY() - round(0.60, 2)

    def leftEdge(self):
        if self.activeState == "layUp":
            return self.layUpRec.getCenter().getX() - round(0.60, 2)
        elif self.activeState == "layDown":
            return self.layDownRec.getCenter().getX() - round(0.60, 2)
        elif self.activeState == "standRight":
            return self.standRightRec.getCenter().getX() - round(0.15, 2)
        elif self.activeState == "standLeft":
            return self.standLeftRec.getCenter().getX() - round(0.15, 2)

    def rightEdge(self):
        if self.activeState == "layUp":
            return self.layUpRec.getCenter().getX() + round(0.60, 2)
        elif self.activeState == "layDown":
            return self.layDownRec.getCenter().getX() + round(0.60, 2)
        elif self.activeState == "standRight":
            return self.standRightRec.getCenter().getX() + round(0.15, 2)
        elif self.activeState == "standLeft":
            return self.standLeftRec.getCenter().getX() + round(0.15, 2)        
    
    def Center(self):
        if self.activeState == "layUp":
            return self.layUpRec.getCenter()
        elif self.activeState == "layDown":
            return self.layDownRec.getCenter()
        elif self.activeState == "standRight":
            return self.standRightRec.getCenter()
        elif self.activeState == "standLeft":
            return self.standLeftRec.getCenter()

    def getFill(self):
        return self.fill

    def undraw(self):
        if self.activeState == "standRight":
            # undraw standRight
            self.standRightRec.undraw()
            self.standRightL1.undraw()
            self.standRightL2.undraw()
            self.standRightL3.undraw()
        elif self.activeState == "layDown":
            # undraw layDown            
            self.layDownRec.undraw()
            self.layDownL1.undraw()
            self.layDownL2.undraw()
            self.layDownL3.undraw()
        elif self.activeState == "standLeft":
            # undraw standLeft
            self.standLeftRec.undraw()
            self.standLeftL1.undraw()
            self.standLeftL2.undraw()
            self.standLeftL3.undraw()        
        elif self.activeState == "layUp":
            # undraw layUp
            self.layUpRec.undraw()
            self.layUpL1.undraw()
            self.layUpL2.undraw()
            self.layUpL3.undraw()

    def type(self):
        return "pole"

    def orientation(self):
        return self.activeState
