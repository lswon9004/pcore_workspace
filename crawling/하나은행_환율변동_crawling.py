from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 창 크기 최대화
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome()

driver.get("https://www.kebhana.com/cont/mall/mall15/mall1503/index.jsp")
time.sleep(2)

driver.switch_to.frame("bankIframe")
#//*[@id="inqFrm"]/table/tbody/tr[1]/td/span/p/label[3]/span
driver.find_element(By.XPATH,'//*[@id="inqFrm"]/table/tbody/tr[1]/td/span/p/label[3]/span').click()

driver.find_element(By.ID, 'tmpInqStrDt_p').clear()
start = '20240701'
driver.find_element(By.ID, 'tmpInqStrDt_p').send_keys(start)

driver.find_element(By.ID, 'tmpInqEndDt_p').clear()
start = '20240722'
driver.find_element(By.ID, 'tmpInqEndDt_p').send_keys(start)

currency = "JPY:100엔(일본)"
driver.find_element(By.ID, 'curCd').send_keys(currency)

driver.find_element(By.XPATH,'//*[@id="inqFrm"]/table/tbody/tr[6]/td/span/p/label[2]').click()

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="HANA_CONTENTS_DIV"]/div[2]/a').click()

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="searchContentDiv"]/div[1]/a[2]/span').click()