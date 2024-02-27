imgfile = open("C:/Users/1DAW-B/Downloads/torre.jpg", "rb")
file_content = imgfile.read()
print("File size is", len(file_content))
imgfile.close()