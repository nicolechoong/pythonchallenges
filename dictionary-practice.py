import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# 1. Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample output of the program when the user enters the data “ThiS is String with Upper and lower case Letters”, would look this this:

def letterCount(string):
    alph = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

    for i in string.lower():
        if i in alph.keys():
            alph[i] += 1

    for i in alph.keys():
        if alph[i] > 0:
            print(i, str(alph[i]))

letterCount("ThiS is String with Upper and lower case Letters")

# 2. Give the Python interpreter’s response to each of the following from a continuous interpreter session:

# >>> d = {"apples": 15, "bananas": 35, "grapes": 12}
# >>> d["bananas"]
# 35

# >>> d["oranges"] = 20
# >>> len(d)
# 4

# >>> "grapes" in d
# True

# >>> d["pears"]
# Error

# >>> d.get("pears", 0)
# 0

# >>> fruits = list(d.keys())
# >>> fruits.sort()
# >>> print(fruits)
# ['apples', 'bananas', 'grapes', 'oranges]

# >>> del d["apples"]
# >>> "apples" in d
# False

def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)

# 3. Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical listing of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland. (You can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.) The first 10 lines of your output file should look something like this:

# 4. What is the longest word in Alice in Wonderland? How many characters does it have?

def alice_words():
    words = {}
    punctuations = 'abcdefghijklmnopqrstuvwxyz '
    text = open("11-0.txt","r")

    for line in text:
        stripped = ""
        for i in line.lower():
            for char in i:
                if char in punctuations:
                    stripped += char
                else:
                    stripped += " "

        list = stripped.split()
        for i in list:
            if i in words:
                words[i] += 1
            else:
                words[i] = 1

    print("Word\t\tCount")
    print("=======================")

    keys = sorted(words.keys())

    for i in keys:
        print(i+"\t\t"+str(words[i]))

    max = 0
    longest = ""
    for i in keys:
        if len(i) > max:
            longest = i
            max = len(i)

    print("\nLongest word: "+longest)

alice_words()
