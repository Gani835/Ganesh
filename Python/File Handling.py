# File Handling:-   To store or to open or to read or to write from a file. .. .  .

f=open("D:\\Sample.txt","r")
print(f)
#f.write("The key function for working with files in Python is the open() function.\n The open() function takes two parameters; filename, and mode.\n There are four different methods (modes) for opening a file:")
f.write('File handling is an important part of any web application.Python has several functions for creating, reading, updating, and deleting files.')
#line=f.readline()
#print(line)
data=f.read()
print(data)


f.close()
