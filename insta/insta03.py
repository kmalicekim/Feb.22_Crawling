from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# selenium : 브라우저 자동화에 사용되는 모듈

input_id = input('id 입력: ')
input_pw = input('pw 입력: ')

service = webdriver.chrome.service.Service('../drivers/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.instagram.com/accounts/login/')
sleep(5)

id = driver.find_element(By.NAME, 'username')   # 맨 처음 찾은 것 하나 / find_elements : 여러개
id.send_keys(input_id)                          # instagram 에서 input 태그안에 name="username"이라고 되어있음

pw = driver.find_element(By.NAME, 'password')
pw.send_keys(input_pw)
sleep(2)

driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3)').click()
# loginForm은 form태그 안이어서 앞에 #
# loginForm 이라는 폼 태그 밑에 div 태그 밑에 3번째 div 태그

# 로그인 버튼이 잘 눌리지 않는다면 아래 코드 작성
sleep(2)
driver.refresh()

later = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
# Copy > Copy full XPath (절대경로)
later.click()
