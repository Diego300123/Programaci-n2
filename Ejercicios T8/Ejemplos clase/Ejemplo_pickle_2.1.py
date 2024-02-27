import sys
import pickle

data_dict = {
    'Brand': 'Porsche',
    'Model': '911'
}

with open(sys.argv[1], 'ab') as myfile:
    data = pickle.dumps(data_dict)
    myfile.write(data)