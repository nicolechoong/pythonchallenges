import random

def randomList(i):
    list = []
    for j in range(0,i):
        list.append(random.randint(0,100))
    return list


def bubbleSort(list):
    print("Unsorted: "+str(list))
    n = len(list)-1
    for i in range(0,len(list)-1):
        for j in range(0,n):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        n = n-1
    print("Sorted: "+str(list))
    return list

bubbleSort(randomList(6))
