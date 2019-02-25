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
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        n = n-1
    print("Sorted: "+str(list))
    return list

bubbleSort(randomList(6))


def bubbleSort2(list):
    count = 0
    print("Unsorted: "+str(list))
    n = len(list)-1
    for i in range(0,len(list)-1):
        for j in range(0,n):
            count += 1
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        n = n-1
    print("Sorted: "+str(list))
    print("Runs: "+str(count))
    return list

bubbleSort2(randomList(6))

def bubbleSort3(list):
    count = 0
    print("Unsorted: "+str(list))
    n = len(list)-1
    for i in range(0,len(list)-1):
        for j in range(0,n):
            count += 1
            print(list)
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        for j in range(0,n):
            if list[j] > list[j+1]:
                break
            elif j == n:
                print("Sorted: "+str(list))
                print("Runs: "+str(count))
                return list
        n = n-1
    print("Sorted: "+str(list))
    print("Runs: "+str(count))
    return list

bubbleSort3([1,2,3,5,4,6])
