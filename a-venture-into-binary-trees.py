class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

# 1. Modify print_tree_inorder so that it puts parentheses around every operator and pair of operands. Is the output correct and unambiguous? Are the parentheses always necessary?

def print_tree_inorder(tree):
    if tree is None: return

    elif tree.left is None and tree.right is None:
        print(tree.cargo, end=" ")
        return

    print(" (", end=" ")
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)
    print(" )", end=" ")


tree = Tree("-", Tree("+", Tree(6), Tree("*", Tree(3), Tree(9))), Tree(1))
print_tree_inorder(tree)

# 2. Write a function that takes an expression string and returns a token list.

def string_token(stringo):
    tokens = []
    tok = ""
    for char in stringo:
        if char not in ''' .?!,;:-()'"@#$%^&*+=[]{}|<>''':
            tok += char
        else:
            tokens.append(tok)
            if char != " ": tokens.append(char)
            tok = ""

    return tokens

print()

print(string_token("Write a function that takes an expression string and returns a token list."))

# 3. Find other places in the expression tree functions where errors can occur and add appropriate raise statements. Test your code with improperly formed expressions.

def get_number(token_list):
    if len(token_list)==0: raise ValueError('No tokens')
    x = token_list[0]
    if type(x) != type(0): return None
    del token_list[0]
    return Tree(x, None, None)

# 4. Think of various ways you might save the animal knowledge tree in a file. Implement the one you think is easiest.

def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animalFileWrite(root):
    file = open("animal.txt","w")
    save(root, file, 0)
    file.close()

def save(root, file, level):
    if root.left is None and root.right is None: return
    save(root.left, file, level+1)
    save(root.right, file, level+1)
    line = root.cargo + "###" + root.left.cargo + "###" + root.right.cargo + "\n"
    file.write(line)

def animal(root = Tree("bird")):
    # Start with a singleton

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("Get dunked on!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

    animalFileWrite(root)

def readLevel(line):
    level = 0
    while line[0] == "*":
        level += 1
    return level

def animalFileRead(path):
    file = open(path, "r")
    forest = {}
    lines = file.readlines()

    for line in lines:
        node = line.split("###")
        node[2] = node[2][:-1]

        for i in range(1,3):
            if node[i] in forest.keys():
                node[i] = forest[node[i]]
            else:
                node[i] = Tree(node[i])

        forest[node[0]] = Tree(node[0],node[1],node[2])
        pokok = Tree(node[0],node[1],node[2])
    print(forest)
    print(pokok.left.left)

    file.close()
    return pokok

# animal()
animal(animalFileRead("animal.txt"))
