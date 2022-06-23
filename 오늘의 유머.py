# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#파일로 저장
f = open("c:\\work\\humor.txt", "a+", encoding="utf=8")

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더)
#웹봇을 막는 경우가 있는데 웹봇이 아니라는 표시를 하기 위해... 비어있지만 않으면 된다.(웹브라우저 헤더 정보)
#아래 Request에 넣는다.
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 주소 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩(utf-8로 해석해보고 조금 깨져도 무시한다.(뺀다))
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # list = soup.find_all('a', attrs={'class':'list_subject'})

# <span class="subject_fixed" data-role="list-title-text" title="아이패드 프로 10.5인치 256기가 와이파이 (전투형, 화이트스팟)">
#         아이패드 프로 10.5인치 256기가 와이파이 (전투형, 화이트스팟)
# </span>

        # for item in list:
        #         try:
        #                 #<a class='list_subject'><span>text</span><span>text</span>
        #                 span = item.contents[1]
        #                 span2 = span.nextSibling.nextSibling  #옆옆 컨텐츠
        #                 title = span2.text 
        #                 if (re.search('아이폰', title)):
        #                         print(title.strip())
        #                         print('https://www.clien.net'  + item['href'])
        #         except:
        #                 pass
        
        list = soup.find_all('td', attrs={'class':'subject'})

#<td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=456276&amp;s_no=456276&amp;page=10" target="_top">세상은 메타버스라는 스님</a>
# <span class="list_memo_count_span"> [39]</span>  <span style="margin-left:4px;">
# <img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span>
#  </td>

        for item in list:
            try:
                title = item.find("a").text
                #title = item.text
                #print(title.strip())
                if (re.search('누리호', title)):
                    print(title.strip())
                    f.write(title.strip()+"\n")
            except:  #광고 때문에 에러나도 넘어가라
                pass

f.close()