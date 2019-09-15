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

# 1. Rewrite the distance function from the chapter titled Fruitful functions so that it takes two Points as parameters instead of four numbers.
def distance(p1, p2):
    dx = p2.y - p1.y
    dy = p2.x - p1.x
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

p1 = Point(3,4)
p2 = Point(6,8)
print(distance(p1,p2))

# 2. Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
# SEE ABOVE

print(Point(3, 5).reflect())

# 3. Add a method slope_from_origin which returns the slope of the line joining the origin to the point. For example,

print(Point(4, 10).slope_from_origin())

# The method will fail if self.x is equal to 0

# 4. The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”). The coefficients a and b completely describe the line. Write a method in the Point class so that if a point instance is given another point, it will compute the equation of the straight line joining the two points. It must return the two coefficients as a tuple of two values.

print(Point(4, 11).get_line_to(Point(6, 15)))

# This method will fail if the two points form a horizontal line

# 5. Given four points that fall on the circumference of a circle, find the midpoint of the circle. When will this function fail?

# If any two points have the same x or y coordinate then this function will fail because you can't divide by 0

# 6. Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone

class SMS_store:

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.inbox.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        unread = []
        for i in range(0,len(self.inbox)):
            (view, num, time, text) = self.inbox[i]
            if not view:
                unread.append(i)
        return unread

    def get_message(self, i):
        try:
            (view, num, time, text) = self.inbox[i]
            self.inbox[i] = (True, num, time, text)
            return (num, time, text)
        except:
            return None

    def delete(self, i):
        self.inbox.remove(i)

    def clear(self):
        self.inbox = []
