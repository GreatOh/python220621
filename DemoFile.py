#DemoFile.py

url = "http://www.credu.com/?page=" + str(1)
print(url)


for x in range(1, 11):
    print(str(x).rjust(3), "*", str(x).ljust(3), "=", str(x*x).center(5))

#0으로 채우기 추가
for x in range(1, 11):
    print(str(x).ljust(3), "*", str(x).rjust(3), "=", str(x*x).zfill(4).center(5))


print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(5340500000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format((4/3)))


#파일을 생성하기
f = open("c:\\work\\demo.txt", "at")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일을 읽기
f = open("c:\\work\\demo.txt", "rt")
result = f.read()
print(result)
f.close()

#파일을 생성하기
f = open("c:\\work\\demo.txt", "a+")
f.write("새로운데이터\n")
f.close()

#한줄씩
f = open("c:\\work\\demo.txt", "rt")
print(f.readline(), end="")
print(f.readline(), end="")
f.seek(0)
lst = f.readlines()
for item in lst:
    print(item.replace("\n", ""))
f.close()
