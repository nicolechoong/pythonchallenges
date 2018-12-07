f = open("poker.txt","r")

dop = {"2":"A", "3":"B", "4":"C", "5":"D", "6":"E", "7":"F", "8":"G", "9":"H", "T":"I", "J":"J", "Q":"K", "K":"L", "A":"M"}
pod = {"A":"2", "B":"3", "C":"4", "D":"5", "E":"6", "F":"7", "G":"8", "H":"9", "I":"T", "J":"J", "K":"Q", "L":"M", "M":"A"}

def valex(d):
    r = []
    for i in d:
        new = dop[i[0]] + i[1]
        r.append(new)
    return sorted(r)

def consec(d):
    let = "ABCDEFGHIJKLM"
    pos = ""
    hc = 0
    e = valex(d)
    for i in e:
        pos += i[0]
    for i in range(0,4):
        for j in range(0,len(let)):
            if pos[i] == let[j]:
                if pos[i:i+5] == let[j:j+5]:
                    return 5
                elif pos[i:i+4] == let[j:j+4]:
                    return 4
                elif pos[i:i+3] == let[j:j+3]:
                    return 3
                elif pos[i:i+2] == let[j:j+2]:
                    return 2
    return 0
    
def rep(d):
    five = False
    four = False
    three = False
    two = False
    pos = ""
    hc = 0
    e = valex(d)
    for i in e:
        pos += i[0]
    for i in range(0,4):
            if pos[i:i+5] == 5*pos[i]:
                five = True
            elif pos[i:i+4] == 4*pos[i]:
                four = True
            elif pos[i:i+3] == 3*pos[i]:
                three = True
            elif pos[i:i+2] == 2*pos[i]:
                if two == "yeet":
                    two = True
                else:
                    two = "yeet"
    if four:
        return 4
    elif three == True and two == True:
        return "fullhouse"
    elif three:
        return 3
    elif two == "yeet":
        return "twopairs"
    elif two:
        return 2

def fl(d):
    if (d[0])[1] == (d[1])[1] == (d[2])[1] == (d[3])[1] == (d[4])[1]:
        return True
    else:
        return False

def sf(d):
    if fl(d) == True and consec(d) == 5:
        return True
    else:
        return False

def rf(d):
    if fl(d) == True and consec(d) == 5 and valex(d)[0][0] == "I":
        return True
    else:
        return False

def highcard(d):
    e = valex(d)
    return pod[e[4][0]]

def woop(d):
    if rf(d):
        return "a"+str(highcard(d))
    elif sf(d):
        return "b"+str(highcard(d))
    elif rep(d) == 4:
        return "c"+str(highcard(d))
    elif rep(d) == "fullhouse":
        return "d"+str(highcard(d))
    elif fl(d):
        return "e"+str(highcard(d))
    elif consec == 5:
        return "f"+str(highcard(d))
    elif rep(d) == 3:
        return "g"+str(highcard(d))
    elif rep(d) == "twopairs":
        return "h"+str(highcard(d))
    elif rep(d) == 2:
        return "i"+str(highcard(d))
    else:
        return "j"+str(highcard(d))

pp1 = 0
while True:
    line = f.readline()
    if len(line) == 0:
        break

    op = line.split()
    p1 = op[0:5].copy()
    p2= op[5:10].copy()
    if woop(p1) < woop(p2):
        pp1 += 1

print(pp1)
