_username = 'liugang'
_password = '123456'

user = input ("please input username:")
pwd = input ("please input password")

if user == _username and pwd == _password:
    print("welcome user %s login" %user)
else:
    print("Wrong username or password")
