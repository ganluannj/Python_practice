import math

def sq(x):
    return x*x


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def distance(self,other):
        return math.sqrt(sq(self.x - other.x)
                         + sq(self.y - other.y))

c = Coordinate(3,4)
Origin = Coordinate(0,0)

#%%
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print (self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
boston_clock.time = '10:30'
paris_clock.print_time()
boston_clock.print_time()


#%%
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        return (self.getX()==other.getX() and self.getY()==other.getY())
    
    def __repr__(self):
        return ("Coordinate(%d, %d)" %(self.getX(), self.getY()))

c1=Coordinate(15,18)
c2=Coordinate(15,18)
print (c1==c2)

print(repr(c1))