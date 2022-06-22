# DemoStr.py

#print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p",9))
print(strA.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("---반복 문구 생성---")
names = ["전우치", "이순신", "머시기"]
for name in names:
    print("안녕하세요 {0}님 더운 여름입니다.".format(name))
    print("="*40)


a = "="*50
print(a)


u = "<<<  spam and ham  >>>"
result = u.strip("<> ")
print(u)
print(result)
result2 = result.replace("spam", "spam egg")
lst = result2.split()
print(lst)
print("---다시 합치기---")
print(" 캬 ".join(lst))