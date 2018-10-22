# minishapes.py
from graphics import*

class miniSquare:
    def __init__(self, center):
        p1 = Point(center.getX() - 0.10,center.getY() - 0.10)
        p2 = Point(center.getX() + 0.10, center.getY() + 0.10)
        self.rec = Rectangle(p1,p2)
        self.rec.setFill("yellow")
        p3 = Point(center.getX(), center.getY() + 0.10)
        p4 = Point(center.getX(), center.getY() - 0.10)
        p5 = Point(center.getX() - 0.10, center.getY())
        p6 = Point(center.getX() + 0.10, center.getY())
        self.l1 = Line(p3, p4)
        self.l2 = Line(p5, p6)
        
    def draw(self, window):
        self.rec.draw(window)
        self.l1.draw(window)
        self.l2.draw(window)

    def undraw(self):
        self.rec.undraw()
        self.l1.undraw()
        self.l2.undraw()

###############################################################################
class miniPole:
    def __init__(self, center):
        p1 = Point(center.getX() - 0.20, center.getY() - 0.05)
        p2 = Point(center.getX() + 0.20, center.getY() + 0.05)
        self.rec = Rectangle(p1, p2)
        self.rec.setFill("aqua")
        # tops of lines
        p3 = Point(center.getX() - 0.10, center.getY() + 0.05)
        p4 = Point(center.getX(), center.getY() + 0.05)
        p5 = Point(center.getX() + 0.10, center.getY() + 0.05)
        # bottoms of lines
        p6 = Point(center.getX() - 0.10, center.getY() - 0.05)
        p7 = Point(center.getX(), center.getY() - 0.05)
        p8 = Point(center.getX() + 0.10, center.getY() - 0.05)

        self.l1 = Line(p3, p6)
        self.l2 = Line(p4, p7)
        self.l3 = Line(p5, p8)

    def draw(self, window):
        self.rec.draw(window)
        self.l1.draw(window)
        self.l2.draw(window)
        self.l3.draw(window)

    def undraw(self):
        self.rec.undraw()
        self.l1.undraw()
        self.l2.undraw()
        self.l3.undraw()

#############################################################################
class miniTshape:
    def __init__(self, center):
        p1 = Point(center.getX() - 0.15, center.getY() - 0.05)
        p2 = Point(center.getX() - 0.05, center.getY() + 0.05)
        p3 = Point(center.getX() + 0.05, center.getY() - 0.05)
        p4 = Point(center.getX() + 0.15, center.getY() + 0.05)
        p5 = Point(center.getX() + 0.05, center.getY() + 0.15)
        self.sq1 = Rectangle(p1, p2)
        self.sq2 = Rectangle(p2, p3)
        self.sq3 = Rectangle(p3, p4)
        self.sq4 = Rectangle(p2, p5)
        self.sq1.setFill("purple")
        self.sq2.setFill("purple")
        self.sq3.setFill("purple")
        self.sq4.setFill("purple")

    def draw(self, window):
        self.sq1.draw(window)
        self.sq2.draw(window)
        self.sq3.draw(window)
        self.sq4.draw(window)

    def undraw(self):
        self.sq1.undraw()
        self.sq2.undraw()
        self.sq3.undraw()
        self.sq4.undraw()

################################################################################
class miniRknight:
    def __init__(self, center):
        p1 = Point(center.getX() - 0.15, center.getY() - 0.05)
        p2 = Point(center.getX() - 0.05, center.getY() + 0.05)
        p3 = Point(center.getX() + 0.05, center.getY() - 0.05)
        p4 = Point(center.getX() + 0.15, center.getY() + 0.05)
        p5 = Point(center.getX() - 0.15, center.getY() + 0.15)
        self.sq1 = Rectangle(p1, p2)
        self.sq2 = Rectangle(p2, p3)
        self.sq3 = Rectangle(p3, p4)
        self.sq4 = Rectangle(p2, p5)        
        self.sq1.setFill("blue")
        self.sq2.setFill("blue")
        self.sq3.setFill("blue")
        self.sq4.setFill("blue")

    def draw(self, window):
        self.sq1.draw(window)
        self.sq2.draw(window)
        self.sq3.draw(window)
        self.sq4.draw(window)

    def undraw(self):
        self.sq1.undraw()
        self.sq2.undraw()
        self.sq3.undraw()
        self.sq4.undraw()
        
###############################################################################
class miniLknight:
    def __init__(self, center):
        p1 = Point(center.getX() - 0.15, center.getY() - 0.05)
        p2 = Point(center.getX() - 0.05, center.getY() + 0.05)
        p3 = Point(center.getX() + 0.05, center.getY() - 0.05)
        p4 = Point(center.getX() + 0.15, center.getY() + 0.05)
        p5 = Point(center.getX() + 0.05, center.getY() + 0.15)
        self.sq1 = Rectangle(p1, p2)
        self.sq2 = Rectangle(p2, p3)
        self.sq3 = Rectangle(p3, p4)
        self.sq4 = Rectangle(p4, p5)        
        self.sq1.setFill("orange")
        self.sq2.setFill("orange")
        self.sq3.setFill("orange")
        self.sq4.setFill("orange")

    def draw(self, window):
        self.sq1.draw(window)
        self.sq2.draw(window)
        self.sq3.draw(window)
        self.sq4.draw(window)

    def undraw(self):
        self.sq1.undraw()
        self.sq2.undraw()
        self.sq3.undraw()
        self.sq4.undraw()

#############################################################################
class miniRhorse:
    def __init__(self, center):
        p1 = Point(center.getX() - 0.15, center.getY() - 0.05)
        p2 = Point(center.getX() - 0.05, center.getY() - 0.15)
        p3 = Point(center.getX() + 0.05, center.getY() - 0.05)
        p4 = Point(center.getX() - 0.05, center.getY() + 0.05)
        p5 = Point(center.getX() + 0.15, center.getY() + 0.05)
        self.sq1 = Rectangle(p1, p2)
        self.sq2 = Rectangle(p2, p3)
        self.sq3 = Rectangle(p3, p4)
        self.sq4 = Rectangle(p3, p5)        
        self.sq1.setFill("lime")
        self.sq2.setFill("lime")
        self.sq3.setFill("lime")
        self.sq4.setFill("lime")

    def draw(self, window):
        self.sq1.draw(window)
        self.sq2.draw(window)
        self.sq3.draw(window)
        self.sq4.draw(window)

    def undraw(self):
        self.sq1.undraw()
        self.sq2.undraw()
        self.sq3.undraw()
        self.sq4.undraw()

##############################################################################
class miniLhorse:
    def __init__(self, center):
        p1 = Point(center.getX() - 0.15, center.getY() - 0.05)
        p2 = Point(center.getX() - 0.05, center.getY() - 0.15)
        p3 = Point(center.getX() + 0.05, center.getY() - 0.05)
        p4 = Point(center.getX() - 0.05, center.getY() + 0.05)
        p5 = Point(center.getX() + 0.15, center.getY() - 0.15)
        self.sq1 = Rectangle(p1, p4)
        self.sq2 = Rectangle(p2, p3)
        self.sq3 = Rectangle(p3, p4)
        self.sq4 = Rectangle(p3, p5)        
        self.sq1.setFill("red")
        self.sq2.setFill("red")
        self.sq3.setFill("red")
        self.sq4.setFill("red")

    def draw(self, window):
        self.sq1.draw(window)
        self.sq2.draw(window)
        self.sq3.draw(window)
        self.sq4.draw(window)

    def undraw(self):
        self.sq1.undraw()
        self.sq2.undraw()
        self.sq3.undraw()
        self.sq4.undraw()
