import pickle

data_list = [1, 2.5, 'Three', False]
print("Original data:", data_list)

bytelist = pickle.dumps(data_list)
print("Converted data:", bytelist)
print(type(bytelist))

original_data = pickle.loads(bytelist)
print("Back to basics:",original_data)