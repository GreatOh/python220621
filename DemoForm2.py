# DemoForm2.py
# DemoForm2.ui(디자인) + DemoForm2.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웹 크롤링
import urllib.request
from bs4 import BeautifulSoup

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼 클래스 정의(QMainWindow)
class DemoForm2(QMainWindow, form_class): # 이 2개를 상속 받았다(다중상속)
    # 생성자 메서드
    def __init__(self):
        super().__init__()  #다중상속받은 모두 초기화 수행
        self.setupUi(self)
    # 슬롯 메서드 정의
    def firstClick(self):
        #파일로 저장
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf=8")

        # 동적으로 주소생성(페이지)
        for i in range(1, 6):
            # 웹페이지의 실행결과를 문자열로 받기
            url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
            print(url)
            data = urllib.request.urlopen(url)
            # 검색을 할 객체 생성
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")

            for item in cartoons:
                title = item.find("a").text
                print(title.strip())
                f.write(title.strip()+"\n")

        f.close()

        self.label.setText("네이버 웹툰 크롤링 종료")
    def secondClick(self):
        self.label.setText("두번째 버튼~~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼~~~")

# 진입점 체크
if __name__ == "__main__": #내가 직접 수행했으면
    # 실행 프로세스
    app = QApplication(sys.argv)  # 이거때문에 sys 를 import
    # 창을 실행
    demoWindow = DemoForm2()
    demoWindow.show()
    # 이벤트 처리 대기
    app.exec_()
