import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

url1 = 'https://www.letskorail.com/korail/com/login.do'
url2 = 'https://www.letskorail.com/ebizprd/EbizPrdTicketPr21111_i1.do'

# 키워드 설정
userid = '2163150929'
passwd = '@dudtjq147'
adult = '어른 1명'
child = '만 6세~12세'
baby = '만 6세 미만'
seat = '창측좌석'
sdirc = '순방향석'
stype = '기본'
dept = '서울'
dest = '부산'
year = '2021'
month = '11'
day = '1'
dtime = '10 (오전10)'

# 셀레니엄 실행
path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
opts = Options()
chrome = webdriver.Chrome(executable_path=path, options=opts)

# 브라우저 창을 최대로 키움
chrome.maximize_window()
time.sleep(1)

# 로그인 페이지로 이동
chrome.get(url1)
time.sleep(1)

# 아이디 입력
# 폼에 자동으로 값을 입력하려면 send_keys 함수를 사용
uid = chrome.find_element(By.ID, 'txtMember')
uid.send_keys(userid)
time.sleep(1)

# 비밀번호 입력
pwd = chrome.find_element(By.ID, 'txtPwd')
pwd.send_keys(passwd)
time.sleep(1)

# 로그인 버튼 클릭
chrome.find_element(By.XPATH, '//img[@alt="확인"]').click()
time.sleep(3)

# 팝업창 자동닫기
# 부모창에서 자식창으로 제어를 이동시킨후 창닫아야 함
# 다시 부모창으로 제어를 이동시켜야 함
# switch_window 함수를 사용하면 창 사이 이동 가능
print(chrome.window_handles) # 화면에 나타난 창 목록 확인

# 첫번째 팝업창으로 제어를 넘긴후 창 닫음
chrome.switch_to.window(chrome.window_handles[1])
chrome.close()
time.sleep(1)
# 메인창으로 제어를 넘김
chrome.switch_to.window(chrome.window_handles[0])
time.sleep(1)

# 열차 예매 페이지로 이동
chrome.find_element(By.XPATH, '//img[@alt="승차권예매"]').click()
time.sleep(2)
# 열차 예매정보 입력
pp01 = Select(chrome.find_element(By.ID, 'peop01'))
pp01.select_by_visible_text(adult)
time.sleep(1)

pp04 = Select(chrome.find_element(By.ID, 'peop04'))
pp04.select_by_visible_text(baby)
time.sleep(1)

elder = '만 65세이상'
pp03 = Select(chrome.find_element(By.ID, 'peop03'))
pp03.select_by_visible_text(elder)
time.sleep(1)

st01 = Select(chrome.find_element(By.ID, 'seat01'))
st01.select_by_visible_text(seat)
time.sleep(1)

st02 = Select(chrome.find_element(By.ID, 'seat02'))
st02.select_by_visible_text(sdirc)
time.sleep(1)

st03 = Select(chrome.find_element(By.ID, 'seat03'))
st03.select_by_visible_text(stype)
time.sleep(1)

# 기차 종류 선택
chrome.find_element(By.XPATH, '//input[@title="KTX"]').click()
time.sleep(1)

# 출발/도착 설정

start = chrome.find_element(By.ID, 'start')
start.clear()
start.send_keys(dept)
time.sleep(1)

get = chrome.find_element(By.ID, 'get')
get.clear()
get.send_keys(dest)
time.sleep(1)

# 출발일 설정
syear = Select(chrome.find_element(By.ID, 's_year'))
syear.select_by_visible_text(year)
time.sleep(1)

smon = Select(chrome.find_element(By.ID, 's_month'))
smon.select_by_visible_text(month)
time.sleep(1)

sday = Select(chrome.find_element(By.ID, 's_day'))
sday.select_by_visible_text(day)
time.sleep(1)

shour = Select(chrome.find_element(By.ID, 's_hour'))
shour.select_by_visible_text(dtime)
time.sleep(1)


# 조회하기 클릭
chrome.find_element(By.XPATH, '//img[@alt="조회하기"]').click()
time.sleep(3)

# 화면 자동 스크롤
chrome.execute_script('window.scrollTo(0.550);')
time.sleep(1)

# 셀레니엄 종료
# chrome.close()

