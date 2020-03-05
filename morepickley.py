import pickle

dummyRecord = "0000"
array = []

for i in range(0,100):
    array.append(dummyRecord)

dummyFile = open("dummy.pickle","wb")
pickle.dump(array, dummyFile)
dummyFile.close()

def checkdummy(loc):
    dummyFile = open("dummy.pickle","rb")
    array = pickle.load(dummyFile)
    dummyFile.close()
    if array[loc] == "0000":
        return True
    else:
        return False

def override(data, loc):
    dummyFile = open("dummy.pickle","rb")
    array = pickle.load(dummyFile)
    array[loc] = data
    dummyFile.close()
    dummyFile = open("dummy.pickle","wb")
    pickle.dump(array, dummyFile)
    dummyFile.close()

print(checkdummy(99))
override("hello", 2)
