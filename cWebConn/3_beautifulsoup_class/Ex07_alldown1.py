"""
    HTML 내부에 있는 링크를 추출하는 함수
        - CSS 파일과 a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse
from urllib import request

# 페이지에 연결되어 있는 링크들을 전부 절대경로의 형태로 return 해줌
# base(url)에 포함되어 있는 링크들을 return 하는 함수
def enum_links(html, base):
    # html : html 구조화된 텍스트가 들어있음 ( url(base)의 페이지 소스 )
    # base : url이 들어있음
    #-------------------------------------
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a[href]')  # href속성을 갖고있는 a태그들을 찾음
    # print(links)
    # print('-'*50)                 
    for a in links:
        href = a.attrs['href']      # 상대경로와 절대경로가 섞여있음
        # print(href)
        url = parse.urljoin(base, href) # url을 절대경로로 변환해줌
        result.append(url)
        # index.html -> https://docs.python.org/3.7/library/index.html
        # ../start.html -> https://docs.python.org/3.7/start.html
        # http://py.com -> http://py.com
    return result
        
if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)