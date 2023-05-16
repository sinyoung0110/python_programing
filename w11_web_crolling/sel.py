import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

#뉴스
driver.get("https://www.naver.com")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(2)
newstitle=driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
print(newstitle)

#부동산
driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("압구정동 현대3차")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]").click()
time.sleep(1)

salesPrices=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]").text
jeonsae=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]").text
print(salesPrices)
print(jeonsae)

#주식
driver.get("https://finance.daum.net/quotes/A005380#influential_investors/home")
time.sleep(2)
lst=[]
for i in range(5):
    price=driver.find_element(By.XPATH,f"/html/body/div/div[4]/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div/table/tbody/tr[{i+1}]/td[4]/span").text
    print(price)
    lst.append(price)

print(lst)

