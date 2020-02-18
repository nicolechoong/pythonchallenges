def hl():
    num = int(input("Please insert a number between 1 and 100\n   > "))
    high = 100
    low = 0
    while low <= high:
        midpoint = (high+low)//2
        exit = input("\nIs your number %d? (Y/N)\n   > " % midpoint)
        if exit == "Y":
            break
        elif midpoint == num:
            print("\nbruh")
            break
        horl = input("\nIs your number higher or lower than %d? (H/L)\n   > " % midpoint)
        if not tomproof(horl, midpoint, num):
            print("\bruh don't lie")
            break
        if horl == "H":
            low = midpoint
        else:
            high = midpoint

# hl()

def hl():
    high = 100
    low = 0
    while low <= high:
        midpoint = (high+low)//2
        exit = input("\nIs your number %d? (Y/N)\n   > " % midpoint)
        if str.upper(exit) == "Y":
            return
        horl = input("\nIs your number higher or lower than %d? (H/L)\n   > " % midpoint)
        if str.upper(horl) == "H":
            low = midpoint+1
        else:
            high = midpoint-1
    print("\nWHY DID YOU CHEAT")

hl()
