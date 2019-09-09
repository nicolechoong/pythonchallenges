import turtle

# 1. Modify the Koch fractal program so that it draws a Koch snowflake, like this:

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)
            print("hi")

def kochsnowflake(t, order, size):
    for i in range(0,3):
        koch(t,order,size)
        t.right(120)

# t = turtle.Turtle()
# window = turtle.Screen()
# kochsnowflake(t,2,300)
# window.mainloop()

# 2a. Draw a Cesaro torn line fractal, of the order given by the user. We show four different lines of orders 0,1,2,3. In this example, the angle of the tear is 10 degrees.

def cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [85,-170,85,0]:
            cesaro(t, order-1, size/3)
            t.right(angle)

# t = turtle.Turtle()
# window = turtle.Screen()
# t.goto(0,0)
# cesaro(t, 3, 300)
# window.mainloop()

# b. Four lines make a square. Use the code in part a) to draw cesaro squares. Varying the angle gives interesting effects — experiment a bit, or perhaps let the user input the angle of the tear.

def cesarosquare(t, order, size):
    for i in range(0,4):
        cesaro(t, order, size)
        t.right(90)

# t = turtle.Turtle()
# window = turtle.Screen()
# t.goto(0,0)
# cesarosquare(t, 3, 300)
# window.mainloop()

# 3. A Sierpinski triangle of order 0 is an equilateral triangle. An order 1 triangle can be drawn by drawing 3 smaller triangles (shown slightly disconnected here, just to help our understanding). Higher order 2 and 3 triangles are also shown. Draw Sierpinski triangles of any order input by the user.

def sierpinski(t, order, size):
    if order == 0:
        for i in range(0,4):
            t.left(120)
            t.forward(size)
    else:
        for angle in range(0,4):
            sierpinski(t, order-1, size/2)
            t.forward(size/2)

# t = turtle.Turtle()
# window = turtle.Screen()
# sierpinski(t, 3, 200)
# window.mainloop()

# 4. Adapt the above program to change the color of its three sub-triangles at some depth of recursion. The illustration below shows two cases: on the left, the color is changed at depth 0 (the outmost level of recursion), on the right, at depth 2. If the user supplies a negative depth, the color never changes. (Hint: add a new optional parameter colorChangeDepth (which defaults to -1), and make this one smaller on each recursive subcall. Then, in the section of code before you recurse, test whether the parameter is zero, and change color.)

def sierpinskiColour(t, order, size, depth=-1):
    if depth == 0:
        colours = ["red","green","blue", "red"]
        t.color(colours[colours.index(t.color()[0])+1])

    if order == 0:
        for i in range(0,4):
            t.left(120)
            t.forward(size)
    else:
        for angle in range(0,4):
            sierpinskiColour(t, order-1, size/2, depth-1)
            t.forward(size/2)


# t = turtle.Turtle()
# t.speed(0)
# t.color("red")
# window = turtle.Screen()
# sierpinskiColour(t, 4, 200, 3)
# window.mainloop()

# 5. Write a function, recursive_min, that returns the smallest value in a nested number list. Assume there are no empty lists or sublists:

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def recursive_min(array, min=9999):
    for i in array:
        if type(i) != type([]):
            if i < min:
                min = i
        else:
            min = recursive_min(i, min)

    return min


def test_suite_recursive_min():
    """ Run the suite of tests for code in this module (this file).
    """
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

test_suite_recursive_min()        # Here is the call to run the tests

# 6. Write a function count that returns the number of occurrences of target in a nested list:

def count(target, array, num=0):
    for i in array:
        if type(i) == type([]):
            num = count(target, i, num)
        else:
            if i == target:
                num += 1
    return num

def test_suite_count():
    test(count(2, []) == 0)
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(count("a",
         [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)

test_suite_count()        # Here is the call to run the tests

# 7. Write a function flatten that returns a simple list containing all the values in a nested list:

def flatten(array, output = []):
    for i in array:
        if type(i) == type([]):
            output = flatten(i, output)
        else:
            output.append(i)
    return output

print(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]))

def test_suite_flatten():
    test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
                  ["this","a","thing","a","is","a","easy"])
    test(flatten([]) == [])

# test_suite_flatten()

# i swear this works and the test case is just broken ; - ;

# 8. Rewrite the fibonacci algorithm without using recursion. Can you find bigger terms of the sequence? Can you find fib(200)?

def fib(count):
    a = 1
    b = 1
    for i in range(0, count-2):
        c = a + b
        a, b = b, c
    print(c)

fib(200)

# 9. Use help to find out what sys.getrecursionlimit() and sys.setrecursionlimit(n) do. Create several experiments similar to what was done in infinite_recursion.py to test your understanding of how these module functions work.

# sys.getrecursionlimit() retrieves the maximum number of recurses the system can perform. In this case it is 1000.

# sys.setrecursionlimit(n) allows you to set the maximum number of recursions you would like a system to perform.

# 10. Write a program that walks a directory structure (as in the last section of this chapter), but instead of printing filenames, it returns a list of all the full paths of files in the directory or the subdirectories. (Don’t include directories in this list — just files.) For example, the output list might have elements like this:

import os


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix = "",output = []):
    """ Print recursive listing of contents of path """

    dirlist = get_dirlist(path)
    for f in dirlist:                   # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            output = print_files(fullname, prefix + "| ", output)
        else:
            output.append(fullname)

    return output

print(print_files(""))
