import copy
mylist = ["gang","li",["ming","xixi"],"xxxx"]
name = ["liugang","tom"]
name3 = name.copy()
name2 = copy.copy(name)
#mylist2 = mylist
'''print(mylist)
print(mylist2)
'''
'''
mylist[1] = "lily"
print(mylist)
print(mylist2)
mylist[2][0] = "min"
print(mylist)
print(mylist2)
'''
for x in mylist:
    print(x)


