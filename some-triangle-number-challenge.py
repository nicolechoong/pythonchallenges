f = open("p042_words.txt")
content = f.read()
f.close()

word = content[1:-1].split('","')

w = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
vv = {}

def trival(w,word,vv):
     for i in range(0,len(word)):
         val = 0
         for j in word[i]:
             val += w[j]
         vv[word[i]] = val
     return vv

def trilistgen():
    n = []
    for t in range(1,100):
        q = 0.5*t*(t+1)
        n.append(q)
    return n

def checktri(vv,n,word):
    tricount = 0
    for f in word:
        if vv[f] in n:
            tricount += 1
    return tricount

trival(w,word, vv)
print("Number of Triangle numbers: "+str(checktri(vv,trilistgen(),word)))
