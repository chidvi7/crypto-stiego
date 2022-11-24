import base64
with open('C:/Users/HP/Desktop/Project/ping.jpg', "rb") as File:
    str1= base64.b64encode(File.read())
    print(str1)
    filename = 's.txt'
    # we are considering a file to store the string.
with open(filename, 'wb') as f:
    f.write(str1)