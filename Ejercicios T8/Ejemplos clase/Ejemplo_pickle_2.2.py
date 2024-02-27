import sys
import pickle

with open(sys.argv[1], 'rb') as myfile:
 
    data = myfile.read()
    orig_data = pickle.loads(data)
    print(orig_data)
    print(type(orig_data))