# web2.py
from turtle import title
import urllib.request
from bs4 import BeautifulSoup


#파일로 저장
f = open("c:\\work\\krx.txt", "wt", encoding="utf=8")

# 동적으로 주소생성(페이지)
# 웹페이지의 실행결과를 문자열로 받기
#url = "https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020301"
url = "http://data.krx.co.kr/contents/MDC/STAT/standard/MDCSTAT022.jsp?menuId=MDC0201020301&viewSequence=0&_=1655967001950"
print(url)
data = urllib.request.urlopen(url)
# 검색을 할 객체 생성
soup = BeautifulSoup(data, "html.parser")
#cartoons = soup.find_all("td", class_="cal-btn-open")
#cartoons = soup.find_all("td", class_="CI-GRID-ALIGN-CENTER" )
cartoons = soup.find_all()

try:
    for item in cartoons:
        #title = item.find("td").text
        title = item.text.replace("\n","")
        print(title.strip())
        f.write(title.strip()+"\n")
except:
    pass


f.close()
print("웹 크롤링 종료")
