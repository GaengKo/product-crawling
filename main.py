import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pyautogui

#from konlpy.tag import Twitter

from selenium.webdriver.common.keys import Keys

#url = 'https://cart.coupang.com/cartView.pang'
#url = 'https://code.plus/lecture/12'
page_num = 0
keyword = 'chair'
url = 'https://www.amazon.com/s?k='+keyword+'&page='+str(page_num)+'&qid=1587970743&ref=sr_pg_'+str(page_num)
print(str(os.getcwd())+'/chromedriver.exe')
DRIVER_DIR = str(os.getcwd())+'/chromedriver.exe'

driver = webdriver.Chrome(DRIVER_DIR)

driver.implicitly_wait(1)
result = []
while page_num < 7:
    page_num = page_num + 1
    url = 'https://www.amazon.com/s?k='+keyword+'&page=' + str(page_num) + '&qid=1587970743&ref=sr_pg_' + str(page_num)
    print(url)
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    subject = soup.select('#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div.s-result-list.s-search-results.sg-row > div')

    print(subject)
    print(len(subject))
    print('--------------------------------------------')
    print(subject[0])
    print('--------------------------------------------')
    #product = BeautifulSoup(subject[0],'html.parser')

    #print(product.select_one('div > div > span > div > div > div.a-section.a-spacing-none.a-spacing-top-small'))
    print('--------------------------------------------')
    #product = subject[0].get_text()
    #print(product.strip())
    if str(subject[0]) == '<div class="s-border-top-overlap aok-hidden"></div>':
        subject = soup.select('#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div.s-main-slot.s-result-list.s-search-results.sg-row > div')
        print(len(subject))
        print('*******************************')
    print('--------------------------------------------')
    for i in range(len(subject)):
        data = []
        try:
            product = subject[i].find('span',class_='a-size-base-plus a-color-base a-text-normal').get_text()
            print(product)
            rating =  subject[i].find('span',class_='a-icon-alt').get_text()
            print(rating)
            review = subject[i].find('span',class_='a-size-base').get_text()
            print(review)
            image = subject[i].find('img').get('src')
            #print(image.get('src'))

        #print(image.get_attribute())
            data.append(product)
            data.append(rating)
            data.append(review)
            data.append(image)
            result.append(data)
        except:
            continue

    #print(html)
with open('./'+keyword+'_1.csv','w',-1,'utf-8',newline='') as f:
    wt = csv.writer(f)
    wt.writerows(result)

"""
driver.find_element_by_name('email').send_keys("oom2024@naver.com")
driver.find_element_by_name('password').send_keys('a1234567890!')
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/div/div/form/fieldset/button').click()
driver.implicitly_wait(10)
time.sleep(2)
#pyautogui.hotkey('alt','F9')
driver.find_element_by_tag_name('iframe')
driver.find_element_by_class_name('play-icon').click()
driver.find_element_by_class_name('fullscreen-icon').click()

print(driver.find_element_by_xpath('//*[@id="player"]/div[7]/div[3]/div[1]/div[3]/div[8]/div').text)

driver.find_element_by_id('login-email-input').send_keys(ID)
time.sleep(0.2)
driver.find_element_by_id('login-password-input').send_keys(str(PW))
time.sleep(0.2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[5]/button').click()
time.sleep(2)
if driver.current_url!='https://cart.coupang.com/cartView.pang':
    print(driver.current_url)
    exit()
while True:
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="cartContent"]/table/thead/tr/th[1]/label/input').click()
        time.sleep(0.5)
        if driver.find_element_by_xpath('//*[@id="cartContent"]/table/thead/tr/th[1]/label/input').get_attribute('checked'):
            driver.find_element_by_xpath('//*[@id="btnPay"]').click()
            time.sleep(0.3)
            driver.find_element_by_xpath('//*[@id="payType7"]').click()
            driver.find_element_by_xpath('//*[@value="KB"]').click()
            driver.find_element_by_xpath('//*[@id="agreement-of-card-agreements"]').click()
            driver.find_element_by_xpath('//*[@id="paymentBtn"]/img').click()
            break
    except Exception as ex:
        driver.refresh()
        print(ex)
    else:
        driver.refresh()"""
#item-select-layer
#/html/body/div[4]/div
#while True:
#    time.sleep(2)
#    pyautogui.press('F5')
