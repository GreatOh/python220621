# web1.py

# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# 문서를 그대로 보기
#print(soup.prettify())

#<P> 태그 전체를 검색
#print(soup.find_all("p"))

#첫번째<P> 태그 검색
#print(soup.find("p"))

#조건이 있는 경우(class 는 충돌 나는데 써야 하므로 언더바를 붙였다)
#print(soup.find_all("p", class_="outer-text"))

# id속성으로 검색
#print(soup.find_all(id="first"))

# 문자열만 리턴
for item in soup.find_all("p"):
    title = item.text  #태그를 없애고 텍스트만
    title = title.replace("\n", "")
    #title = title.replace(" ", "")
    #title = item.find("a").text
    print(title.strip())