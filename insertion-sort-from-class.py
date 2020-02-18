array = [5,2,3,6,1,4]

def insertion(array):
    for i in range(1,len(array)):
        for j in range(0,len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array.pop(i)
                array.insert(j, temp)
                break

insertion(array)
