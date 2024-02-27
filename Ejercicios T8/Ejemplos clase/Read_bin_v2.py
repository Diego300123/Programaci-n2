imgfile = open("asd.jpg", "rb")
file_content = imgfile.read()
print("File size is", len(file_content))
imgfile.close()