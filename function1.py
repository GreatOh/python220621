# function1.py

def times(a,b):
    return a+b, a*b;


result = times(3, 4)
print(result)


a=1.2
print(id(a))
a=2.3
print(id(a))

lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))


def change(x):
    x[0] = "H"

wordlist=['J', 'A', 'M']
change(wordlist)
print("함수 호출 후:", wordlist)


def change2(x):
    #복사본(Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)


wordlist=['J', 'A', 'M']
change2(wordlist)
print("함수 호출 후:", wordlist)


#교집합 함수(디버깅 연습 - return이 어디에 있느냐에 따라서 결과가 다르다)
def intersect(prelist, postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM", "SPAM"))


def times(a=10, b=20):
    return a*b

print(times())

def times(a, b):
    return a*b

print(times(b=9, a=8))