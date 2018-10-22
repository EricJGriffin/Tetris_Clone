# square.py
# a tetris square
from graphics import *

class Square:
    """ This version is going to initialize the square using setCoords."""
    
    def __init__(self, window):
        #square should start at center top of the screen
        #p1 and p2 create rectangle
        p1 = Point(3.20,6.50)
        p2 = Point(3.80,7.10)
        #p3, p4, p5 and p6 are for the lines in the square
        p3 = Point(3.50,7.10)
        p4 = Point(3.50,6.50)
        p5 = Point(3.20,6.80)
        p6 = Point(3.80, 6.80)
        self.rec = Rectangle(p1, p2)
        self.rec.fill = "yellow"
        self.rec.setFill(self.rec.fill)
        self.line1 = Line(p3, p4)
        self.line1.setFill(color_rgb(25,25,25))
        self.line2 = Line(p5, p6)
        self.line2.setFill(color_rgb(25,25,25))
        self.rec.draw(window)
        self.line1.draw(window)
        self.line2.draw(window)

        self.rec.setWidth(2)
        self.line1.setWidth(2)
        self.line2.setWidth(2)

    def move(self, key):
        if key == "Right":
            self.rec.move(0.30,0.0)
            self.line1.move(0.30,0.0)
            self.line2.move(0.30,0.0)
        if key == "Left":
            self.rec.move(-0.30,0.0)
            self.line1.move(-0.30,0.0)
            self.line2.move(-0.30,0.0)
        if key == "Down":
            self.rec.move(0.0,-0.30)
            self.line1.move(0.0,-0.30)
            self.line2.move(0.0,-0.30)

    def bottomEdge(self):
        return self.rec.getCenter().getY() - 0.3

    def leftEdge(self):
        return self.rec.getCenter().getX() - 0.3

    def rightEdge(self):
        return self.rec.getCenter().getX() + 0.3

    def Center(self):
        return self.rec.getCenter()
    def getFill(self):
        return self.rec.fill

    def undraw(self):
        self.rec.undraw()
        self.line1.undraw()
        self.line2.undraw()
    
    def type(self):
        return "square"
    
        
