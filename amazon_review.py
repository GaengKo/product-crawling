import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import io
import csv
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = 'https://www.amazon.com/s?k=robot+vaccume'
print(str(os.getcwd())+'/chromedriver.exe')
DRIVER_DIR = str(os.getcwd())+'/chromedriver.exe'

driver = webdriver.Chrome(DRIVER_DIR)
driver.implicitly_wait(1)
result = []
driver.get(url)
driver.implicitly_wait(10)
print('제품 페이지를 선택한 후 아무 키와 엔터를 누르면 크롤링을 시작합니다 : ')
a = input()

html = driver.page_source
#soup = BeautifulSoup(html, 'html.parser')

try:
    driver.find_element_by_xpath('//*[@id="cr-pagination-footer-0"]/a').click()
except:
    driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a').click()
driver.implicitly_wait(10)
result = []
product_name = driver.find_element_by_xpath('//*[@id="cm_cr-product_info"]/div/div[2]/div/div/div[2]/div[1]/h1/a').text
qwe = 0
while True:
    a = driver.find_element_by_xpath('//*[@id="cm_cr-review_list"]')
    customer_review = a.find_elements_by_xpath('div')
    #customer_review_title = a.find_elements_by_xpath('div/div/div[2]/a[2]/span')
    temp = 0
    for i in range(len(customer_review)):
        if i >= 10:
            break
        else :
            review_temp = []
            try:
                try:
                    customer_review_title = customer_review[i + temp].find_element_by_xpath('div/div/div[2]/a[2]/span')
                    customer_review_rate = customer_review[i + temp].find_element_by_xpath('div/div/div[2]/a[1]')
                    customer_review_text = customer_review[i + temp].find_element_by_xpath('div/div/div[4]/span')
                except:
                    temp = 1
                    customer_review_title = customer_review[i + temp].find_element_by_xpath('div/div/div[2]/a[2]/span')
                    customer_review_rate = customer_review[i + temp].find_element_by_xpath('div/div/div[2]/a[1]')
                    customer_review_text = customer_review[i + temp].find_element_by_xpath('div/div/div[4]/span')
                print(customer_review_title.text)
                print(customer_review_rate.get_attribute('title'))
                print(customer_review_text.text)
                print(qwe*10 + i + temp)
                review_temp.append(customer_review_title.text)
                review_temp.append(customer_review_rate.get_attribute('title'))
                review_temp.append(customer_review_text.text)
                result.append(review_temp)
            except:
                break
    try:
        if driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').is_enabled():
            driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
        else:
            break;
        time.sleep(1)
    except Exception as e:
        print(e)
        break
    qwe = qwe + 1

print(result[0][1])
print('create xlsx file...')
df = pd.DataFrame(result,columns=['title','rate','text'])
df.to_excel('./amazon_review/'+product_name+'.xlsx',index=False)
df.to_excel('./amazon_review/SaveCacheData.xlsx',index=False)

#a = driver.find_elements_by_css_selector('#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div > div > span > div > div > div > div > div:nth-child(2) > div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28 > div > div:nth-child(1) > div > div > div.a-section.a-spacing-none.a-spacing-top-micro > div > span:nth-child(2) > a')
#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2) > div > span > div > div > div > div > div:nth-child(2)
#print(len(a))
#for i in range(len(a)):
#    print("i")
##    a[i+1].click()
##    time.sleep(5)
#    driver.back()
#    time.sleep(8)

#print(a)
#print(len(a))