info = {
    "st01":"liugang",
    "st02":"tom",
    "st03":"lily"
}

print(info) #字典无序的
print(info["st01"])
info["st01"] = "liugang2" #modify
print(info["st01"])
info["st04"] = "kite" #add
print(info)

#find
print(info.get("st0001")) #None

print("st05" in info)
print(info)

#del
del info["st04"]
print(info)

#del2
info.pop("st03")
print(info)

#del3
info.popitem() #随意删除


#字典嵌套
av_catalog = {

    "erop":{
        "www.youporn.com":["good"],
        "www.xxx.com":["bad"]

    },
    "jp":{
        "tokyo-hot":["goood"]

    },
    "cn":{
        "1024":["free"]
    }
}
av_catalog["cn"]["1024"][0] = "good and free!!"
print(av_catalog)