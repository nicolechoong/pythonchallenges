import pickle

example = [1,1,1,1]

pickle_out = open("hello.pickle","wb")
pickle.dump(example, pickle_out)
pickle_out.close()

pickle_in = open("hello.pickle","rb")
example_list = pickle.load(pickle_in)

print(example_list)
