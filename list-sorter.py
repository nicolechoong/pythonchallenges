myfile = open("A207s1.txt", "w")
wl = input("Please input a list of words   > ")
w = wl.split()
w = sorted(w)
w = " ".join(w)
myfile.write(w)
myfile.close()