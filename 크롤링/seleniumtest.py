from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# 다음 영화 사이트에서 영화제목, 평점, 예매율 추출하기
url = 'https://movie.daum.net/main'

# headless를 위한 설정
options = Options()
options.add_argument('--headless')

# 크롬 webdriver 설정
path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
#chrome = webdriver.Chrome(executable_path=path)    # 브라우저가 뜨는 것이 보임
chrome = webdriver.Chrome(executable_path=path, options=options)

# 지정한 url로 접속
chrome.get(url)

# 응답받은 소스 출력
# print(chrome.page_source)
res = chrome.page_source

# 크롬 웹드라이버 종료
chrome.close()

# 읽어들인 페이지소스를 BeautifulSoup로 파싱
html = BeautifulSoup(res, 'lxml')

# 영화제목 추출
for title in html.select('strong.tit_item a'):
    print(title.text)

# 영화평점 출력
for rate in html.select('span.txt_append span:first-child'):
    print(rate.text)

# 영화예매율 출력
for resrv in html.select('span.txt_append span:last-child'):
    print(resrv.text)










