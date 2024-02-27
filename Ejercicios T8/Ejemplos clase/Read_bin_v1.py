imgfile = open('asd.jpg', 'rb')
total_size = 0
chunk_size = 1024

data = imgfile.read(chunk_size)

total_size += len(data)

while data:
    data = imgfile.read(chunk_size)
    if data:
        total_size += len(data)

imgfile.close()
print("The size is:", total_size)