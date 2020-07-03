"""
    [ 굽네치킨 매장 주소 가져오기 ]

    굽네치킨 http://www.goobne.co.kr > 매장찾기 > 매장찾기
                  http://www.goobne.co.kr/store/search_store.jsp

    개발자모드( F12 ) 열고 페이지 번호를 누르면
    <tbody> 부분이 교체되는 것을 볼 수 있다

    또한 2번 페이지 번호에 <a href="javascript:store.getList('2');">2</a>로 자바스트립트 함수를 호출한다.

    이 때 WebDriver 라는 특정 웹 브라우저의 원격 제어 인터페이스를 이용하고
    selenium 패키지를 이용하여  DOM  요소를 가져오거나 자바스크립트에서 제어하는 동작을 할 수 있도록 한다.
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
#-------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3)

for i in range(1, 10):
    # 페이지 접근
    driver.get('http://www.goobne.co.kr/store/search_store.jsp')
    driver.execute_script('store.getList({0})'.format(i)) # 홈페이지에서 페이지 버튼을 누를경우 실행되는 스크립트
    
    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    for store_list in soup.findAll('tbody', attrs={'id':'store_list'}):
        name = soup.select('tr > td:first-child')
        tel = soup.select('.store_phone > a')
        addr = soup.select('.t_left > a')
        print("tel", tel)
        for n, t, a in zip(name, tel, addr):
            print(n.text, " - ", t.text, "-", a.text)
        #print(name.text, ":")

