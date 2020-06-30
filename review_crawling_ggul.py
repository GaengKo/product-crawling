import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup

import csv

url = 'https://www.ggulreview.com/p/robotic-vacuums'
print(str(os.getcwd())+'/chromedriver.exe')
DRIVER_DIR = str(os.getcwd())+'/chromedriver.exe'

driver = webdriver.Chrome(DRIVER_DIR)

driver.implicitly_wait(1)
result = []
driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="__next"]/div/div/nav/span/div/a').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/a[1]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys('accuracy@kakao.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys('-')
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()

driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[7]/div/div').click() #더보기
time.sleep(3)
driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[7]/div/div').click() #더보기
time.sleep(3)
driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[7]/div/div').click() #더보기
time.sleep(3)
driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[7]/div/div').click() #더보기
time.sleep(3)

Crawling_Data = []
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
a = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[7]/div/ul')
products = soup.select('#__next > div > main > div:nth-child(7) > div > ul > li > a')
p_products = driver.find_elements_by_xpath('//*[@id="__next"]/div/main/div[7]/div/ul/li/a')
print(p_products)
print(len(p_products))
for i in range(len(p_products)):
    Crawling_Data.append([])
    product_text = driver.find_element_by_css_selector('#__next > div > main > div:nth-child(7) > div > ul > li:nth-child('+str(i+1)+') > a > div.product-list-item__content > div.product-list-item__desc').text
    Crawling_Data[i].append(product_text)
    Crawling_Data[i].append([])
    Crawling_Data[i].append([])
    print()
    driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[7]/div/ul/li['+str(i+1)+']/a').click() #제품 클릭

    driver.implicitly_wait(3)
    time.sleep(1)
    num_of_review = driver.find_element_by_xpath('//*[@id="__next"]/div/main/nav/a[3]').text
    print(num_of_review)
    if num_of_review != '실사용 리뷰 0':
        driver.find_element_by_xpath('//*[@id="__next"]/div/main/nav/a[3]').click()  #실사용 리뷰 클릭
        driver.implicitly_wait(3)
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[8]/div/div[4]/button').click()
            time.sleep(2)
            while True:
                driver.find_element_by_css_selector('#__next > div > div.reviews-list__wrapper > div.reviews-list > div.reviews-list__more').click()
                time.sleep(2)
        except:
            pass
        if int(num_of_review.split(' ')[2]) > 2:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            subject = soup.select('#__next > div > div.reviews-list__wrapper > div.reviews-list > div > div > div.product-reviews__item__proscons__wrapper > p')
            for j in range(len(subject)):
                asd = subject[j].find_all('span')
                temp_index = 0
                for k in asd:
                    if k.get_text() != '...':
                        Crawling_Data[i][temp_index+1].append(k.get_text())
                        print(k.get_text())
                        temp_index = temp_index + 1
                print()
            driver.back()
            driver.implicitly_wait(3)
        else:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            subject = soup.select('#__next > div > main > div > div > div > div > div.product-reviews__item__proscons__wrapper > p')
            for j in range(len(subject)):
                asd = subject[j].find_all('span')
                temp_index = 0
                for k in asd:
                    if k.get_text() != '...':
                        Crawling_Data[i][temp_index + 1].append(k.get_text())
                        print(k.get_text())
                        temp_index = temp_index + 1
                print()
    driver.back()
    driver.implicitly_wait(3)
    time.sleep(1)

#print(len(products))
#print(products)
print(Crawling_Data)
for i in Crawling_Data:
    pn = i[0].split('\n')
    product_name = pn[0]+'_'+pn[1]
    f = open('./review/'+product_name + "_장점 리뷰.txt", 'w', -1, "utf-8")
    for j in i[1]:
        f.write(j+'\n')
    f.close()

    f = open('./review/'+product_name + "_단점 리뷰.txt", 'w', -1, "utf-8")
    for j in i[2]:
        f.write(j + '\n')
    f.close()

#for product in products:
#    print(product.get_text())
#    b = product.find('a')
#    print(b)
#    print(product['href'])
#    #print(b.attrs['href'])

#product = soup.fi
"""
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
            review = subject[i].find_all('span',class_='a-size-base')
            for j in review:
                if (j.get_text()).replace(',','').isdigit():
                    review = j.get_text()
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
