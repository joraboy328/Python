data = {

    'beijin':{
        'changping':{
            "guomao":["xx","bb"],
            "tiandu":{"xxx","yyy"}
        }

    },
    'jiangsu': {
        'nantong': {
            "chongchuan": ["wanda", "jinbaobei"],
            "gangzha": {"huoguo", "ruchuan"}
        },
        'suzhou':{
            "def":["xxxxxxx","y"],
            "abc":["xxxx","yyyyy"]
        }


    }
}

while True:
 for i in data:
    print(i)
 choice = input("please input=>")
 if choice in data:
    while True:
        for i2 in data[choice]:
            print("\t",i2)
        choice2 = input("please input=>")
        if choice2 in data[choice]:
            while True:
                for i3 in data[choice][choice2]:
                    print("\t",i3)
                choice3 = input("please input=>")
                if choice3 in data[choice][choice2]:
                  for i4 in data[choice][choice2][choice3]:
                    print(i4, "\t\t")
                  choice4 = input("Press B return>>")
                  if choice4 == "b":
                    pass
                if choice3 == "b":
                    break
        if choice2 == "b":
            break








