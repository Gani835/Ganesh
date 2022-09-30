##  OS Module  ##

# Def:- python os module is used to interact with the operating system.

# Examples:-

'''import os
path=os.getcwd()        # cwd means current working directory.
print(path)                 # It returns the current directory.


import os
os.chdir('D:/')             # Change direwctory to D drive.
path=os.getcwd()
print(path)                 # It returns D drive.


import os
os.mkdir('Newdir')      # To create a new directory.


import os
if os.path.isdir('D:\\Newdir'):
    print("Boss directory already created")      # To check the directory exist or not.
else:
    os.mkdir('Newdir')


import os
for file in os.listdir(os.getcwd()):       #  To display all files in our directory.
    print(file)
'''




'''import os
path=os.getcwd()
print(path)


import os
os.chdir('E:/')
path=os.getcwd()
print(path)



import os
os.chdir('D:/')
path=os.getcwd()
print(path)


import os
os.mkdir('Newdir2')


import os
if os.path.isdir('D:\\Newdir2'):
    print("Boss directory already created")
else:
    os.mkdir('Newdir2')
'''

import os
for file in os.listdir(os.getcwd()):
    print(file)































