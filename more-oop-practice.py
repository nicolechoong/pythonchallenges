class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def reflect(self):
        return self.x, -self.y

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, target):
        m = (self.y - target.y)/ (self.x - target.x)
        c = self.y - m*self.x
        return m, c

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        return self.width*self.height

    def perimenter(self):
        return 2*self.width + 2*self.height

    def flip(self):
        (self.width, self.height) = (self.height, self.width)

    def contains(self, point):
        if point.x < self.corner.x + self.width and point.x >= self.corner.x and point.y < self.corner.y + self.height and point.y >= self.corner.y:
            return True
        else:
            return False

    def collision(self, rect):
        xrange = (self.corner.x, self.corner.x + self.width)
        yrange = (self.corner.y, self.corner.y + self.height)

        if (xrange[0] <= rect.corner.x and xrange[1] > rect.corner.x) or (xrange[0] <= rect.corner.x + rect.width and xrange[1] > rect.corner.x + rect.width) or (yrange[0] <= rect.corner.y and yrange[1] > rect.corner.y) or (yrange[0] <= rect.corner.y + rect.height and yrange[1] > rect.corner.y + rect.height):
            return True
        else:
            return False



# 1. Add a method area to the Rectangle class that returns the area of any instance:

r = Rectangle(Point(0, 0), 10, 5)
print(r.area())

# 2. Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance:

# 3. Write a flip method in the Rectangle class that swaps the width and the height of any rectangle instance:

# 4. Write a new method in the Rectangle class to test if a Point falls within the rectangle. For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on the width and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is excluded, and from [0 to 5) in the y direction. So it does not contain the point (10, 2). These tests should pass:

# 5. In games, we often put a rectangular “bounding box” around our sprites. (A sprite is an object that can move about in the game, as we will see shortly.) We can then do collision detection between, say, bombs and spaceships, by comparing whether their rectangles overlap anywhere.

# Write a function to determine whether two rectangles collide. Hint: this might be quite a tough exercise! Think carefully about all the cases before you code.
