from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
# browser.maximize_window() # 창최대화 

url = "https://flight.naver.com"
browser.get(url)

#가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일 28일 선택

browser.find_elements_by_link_text("12")[0].click() #elements 복수인거조심
browser.find_elements_by_link_text("15")[0].click()


#제주도선택

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()


# 항공권 검색 클릭

browser.find_element_by_link_text("항공권 검색").click()

#재우기
# time.sleep(3)


#나올때까지만
try:                                                                          
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    #성공했을때 동작 수행
    print(elem.text)        # 첫번째 결과 출력
finally:
    browser.quit()

#첫번쨰 결과 출력
# elem = browser.find_element_by_link_xpath("//'[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)