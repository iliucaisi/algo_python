import pickle

data = ['Help me!', 123.456, True]

# python 2.x
# f = open('test.data', 'w')

# python 3.x
f = open('test.data', 'wb+')

pickle.dump(data, f)
f.close()

f = open('test.data', 'rb+')
data = pickle.load(f)
print(data)
f.close()
