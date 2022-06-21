# function2.py

x=2

def func(a):
    return a+x

print(func(1))

def func2(a):
    x=1
    return a+x

print(func2(1))
print(x)


def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("credu.com", "80"))
print(connectURI(port="8080", server="credu.com"))


def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))


def userURIBuilder(server, port, **user):
    str="http://"+ server + ":"+port+"/?"
    for key in user.keys():
        str += key + "=" + user[key]+"&"
    return str

print(userURIBuilder("credu.com", "80", id="kim", passwd="1234"))
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234", name="mike"))



g=lambda x,y:x*x
print(g(2,3))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())
