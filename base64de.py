import base64
with open('s.txt', "rb") as File:
    str1= (File.read())
    imgdata = base64.b64decode(str1)
    filename = 'C:/Users/HP/Desktop/Project/pingsss.jpg'
with open(filename, 'wb') as f:
    f.write(imgdata)