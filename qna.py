import pickle

try:
    picfile = open("qnapickle.pickle","rb")

except:
    picfile = open("qnapickle.pickle","wb")
    array = []
    file = open("Past Paper 4 Guesswork - Sheet1 (1).tsv","r")
    for line in file:
        array.append(line.split("	"))
    pickle.dump(array, picfile)

picfile.close()

picfile = open("qnapickle.pickle","rb")
array = pickle.load(picfile)
picfile.close()

for q in range(1, len(array)):
    if len(array[q]) == 5:
        print("\nQuestion: "+array[q][0])
        a = input("\nPlease input your answer\n   > ")
        print("\nMark scheme:")
        print(array[q][2])
        m = input("\nPlease input your mark\n   > ")
        array[q].append(m)
        picfile = open("qnapickle.pickle","wb")
        pickle.dump(array, picfile)
        picfile.close()

picfile = open("qnapickle.pickle","rb")
array = pickle.load(picfile)

score = 0
for q in array[1:]:
    score += int(q[5])
print("Score: "+str(score)+"/72")

picfile.close()
