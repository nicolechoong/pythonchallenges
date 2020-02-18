def binarySearch(Array, searchItem):
    First = 0
    Last = len(Array)-1
    Found = False

    while First <= Last and not Found:
        Midpoint = (First + Last) // 2
        if Array[Midpoint] == searchItem:
            Found = True
        else:
            if Array[Midpoint] > searchItem:
                Last = Midpoint - 1
            else:
                First = Midpoint + 1

    if not Found:
        return False
    else:
        return True

print(binarySearch([1,2,3,4,5,6,7], 7))
print(binarySearch([1,2,3,4,5,6,7], 70))
