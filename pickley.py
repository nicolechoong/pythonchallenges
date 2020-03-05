import pickle

example = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}

pickle_out = open("hello.pickle","wb")
pickle.dump(example, pickle_out)
pickle_out.close()

def convert(binary):
    pickle_in = open("hello.pickle","rb")
    translate = pickle.load(pickle_in)
    chunks = binary.split()
    for i in chunks:
        print(translate[i], end = " ")

convert("0110 1101 0101")
