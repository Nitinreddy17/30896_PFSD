'''

try:
    a = open("file.txt")
    try:
        a.write("This is Helsinki")
    finally:
        a.close()
except IOError:
    print("File not found")
else:
    print("The File Opened")
    a.close()


'''



try:
    a = open("file.txt", "w")
    try:
        a.write("This is Helsinki")
    finally:
        a.close()
except IOError:
    print("File not found")
else:
    print("The File Opened")
    a.close()