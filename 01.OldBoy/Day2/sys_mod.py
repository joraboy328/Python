import os

#result = os.system("ls -l")
result = os.popen("ls -l").read()
print (result)
os.mkdir("mytest")