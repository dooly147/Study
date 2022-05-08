# k-apt.go.kr

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = 'https://k-apt.go.kr'

# headless를 위한 설정
options = Options()
# options.add_argument('--headless')

# webdriver 실행
path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
#chrome = webdriver.Chrome(executable_path=path)
chrome = webdriver.Chrome(executable_path=path, options=options)

# 소스 읽어오기
chrome.get(url)

# 소스가 다 로딩될 때까지 2초정도 대기
chrome.implicitly_wait(2)
time.sleep(2)   # 작업을 의도적으로 지연 (2초동안)

# 팝업창 닫기 #1 - css 선택자
# find_element_by_css_selector(대상).click()
#chrome.find_element_by_css_selector('#popup_20210518 div.layerPopupTitle div a').click()
#time.sleep(1)

#chrome.find_element_by_css_selector('#popup_20200720_02 div.layerPopupTitle div a').click()
#time.sleep(1)

# 팝업창 닫기 #2 - 자바스크립트 함수 호출
# execute_script(함수명)
#chrome.execute_script('closeLyserPopup("popup_20200720_02")')
#time.sleep(1)

#chrome.execute_script('closeLyserPopup("popup_20210518")')
#time.sleep(1)

# 팝업창 닫기 #2b - 자동으로 자바스크립트 함수 호출
pops = chrome.find_elements_by_css_selector('div.layerPopup')
for pop in pops:
    id = pop.get_attribute('id')   # 지정한 요소의 id값을 알아냄
    js = f'closeLyserPopup("{id}")'
    chrome.execute_script(js)
    time.sleep(1)

# '단지정보' 클릭
chrome.find_element(By.CSS_SELECTOR, '#lnbMenu > li:nth-child(2) > a').click()
time.sleep(2)

# 참고
# selector copy : group_date > select.combo_YYYY > option:nth-child(11)
# XPath copy : //*[@id="group_date"]/select[1]/option[11]

# 검색할 단지정보 선택 - 2021-10, 서울특별시, 구로구, 구로동, LG신도림자이
chrome.find_element(By.XPATH, '//*[@title="년도 선택"]/option[text()="2021"]').click()
time.sleep(1)

chrome.find_element(By.XPATH, '//*[@title="월 선택"]/option[text()="10"]').click()
time.sleep(1)

chrome.find_element(By.XPATH, '//*[@title="광역시도 선택"]/option[text()="서울특별시"]').click()
time.sleep(1)

chrome.find_element(By.XPATH, '//*[@title="시군구 선택"]/option[text()="구로구"]').click()
time.sleep(1)

chrome.find_element(By.XPATH, '//*[@title="읍면동 선택"]/option[text()="구로동"]').click()
time.sleep(1)

chrome.find_element(By.XPATH, '//*[@title="LG신도림자이"]').click()
time.sleep(1)

# 관리시설정보 클릭
chrome.find_element(By.XPATH, '//*[@alt="관리시설정보"]').click()
time.sleep(1)

# 단지 상세정보에서 '주차대수' 추출
park = chrome.find_element(By.XPATH, '//*[@id="parking_cnt"]').text
print(park)

# chrome 닫기
#time.sleep(1)
#chrome.close()


