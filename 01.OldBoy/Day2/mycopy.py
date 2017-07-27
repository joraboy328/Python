import copy

name = ["liugang",["lily","wu","xxx"],"wuxi"]
name2 = name.copy()
name3 = copy.deepcopy(name)
name[0] = "liugang2"
name[1][0] = "lily2"
print(name,name2)
print(name3)


