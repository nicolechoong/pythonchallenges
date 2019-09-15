# 1. Write a function named readposint that uses the input dialog to prompt the user for a positive integer and then checks the input to confirm that it meets the requirements. It should be able to handle inputs that cannot be converted to int, as well as negative ints, and edge cases (e.g. when the user closes the dialog, or does not enter anything at all.)

def readposint():
    num = input("Please enter your age: ")
    try:
        num = int(num)
    except:
        raise ValueError("{0} is not an integer".format(num))
    if num < 0:
        error = ValueError("{0} is not a positive integer".format(num))
        raise error
    return num

readposint()
