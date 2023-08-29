#!/usr/bin/env python
# coding: utf-8

# # 라이브러리 설치

# In[ ]:


get_ipython().system('pip install selenium')


# In[2]:


import sys
print(sys.executable)


# In[1]:


get_ipython().system('C:\\ProgramData\\Anaconda3\\python.exe -m pip install selenium')


# # Selenium 연습

# ## By.Name 구문

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# ChromeDriver의 경로를 지정하고, WebDriver 인스턴스를 생성합니다.
driver = webdriver.Chrome()

# 지마켓의 메인 페이지를 엽니다.
driver.get('https://www.gmarket.co.kr')

# 검색어를 입력할 수 있는 input 요소를 찾습니다.
search_box = driver.find_element(By.NAME, 'keyword')

# 검색어를 입력하고, Enter 키를 눌러 검색을 실행합니다.
search_box.send_keys('손풍기')
search_box.send_keys(Keys.RETURN)

# 작업이 끝나면 WebDriver를 종료하여 브라우저 창을 닫습니다.
driver.quit()


# ## By.CSS_SELECTOR 구문

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

title_list = list()

# ChromeDriver의 경로를 지정하고, WebDriver 인스턴스를 생성합니다.
driver = webdriver.Chrome()

# 지마켓의 베스트 페이지를 엽니다.
driver.get('https://www.gmarket.co.kr/n/best')

# 상품명을 입력 받아 item_list 변수에 저장합니다.
item_list = driver.find_elements(By.CSS_SELECTOR, 'a.itemname')

for item in item_list:
    title_list.append(item.text)

driver.quit()


# In[10]:


print(title_list)


# # selenium 실행하고 상품명, 가격, 별점 정보 저장

# In[11]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

title_list = list()
price_list = list()
star_list = list()

# ChromeDriver의 경로를 지정하고, WebDriver 인스턴스를 생성합니다.
driver = webdriver.Chrome()

# 지마켓의 메인 페이지를 엽니다.
driver.get('https://www.gmarket.co.kr')

# 검색어를 입력할 수 있는 input 요소를 찾습니다.
search_box = driver.find_element(By.NAME, 'keyword')

# 검색어를 입력하고, Enter 키를 눌러 검색을 실행합니다.
search_box.send_keys('손풍기')
search_box.send_keys(Keys.RETURN)

# 결과 페이지가 로드될 때까지 잠시 기다립니다.
driver.implicitly_wait(3)

# 정보를 담은 박스를 선택합니다.
search_results = driver.find_elements(By.CSS_SELECTOR, 'div.box__information')

for result in search_results:
    #만족도가 없을 수도 있기에 try except문을 활용
    try:
        title_element = result.find_element(By.CSS_SELECTOR, 'span.text__item')
        price_element = result.find_element(By.CSS_SELECTOR, 'div.box__price-seller > strong')
        star_element = result.find_element(By.CSS_SELECTOR, 'span.image__awards-points > span')
        title_list.append(title_element.text)
        price_list.append(price_element.text)
        star_list.append(star_element.text)
    except:
        pass
    
# 작업이 끝나면 WebDriver를 종료하여 브라우저 창을 닫습니다.
driver.quit()


# # 데이터 프레임으로 저장하고 Excel 파일로 저장하기

# In[17]:


import pandas as pd

gmarket_selenium_df = pd.DataFrame([title_list, price_list, star_list]).T


# In[18]:


gmarket_selenium_df.columns = ['상품명', '판매가', '만족도']


# In[19]:


gmarket_selenium_df


# In[20]:


def extract_comma(x):
    price = int(x.replace(",", "")) #replace로 쉼표까지 제거하고 int로 변환
    return price


# In[21]:


gmarket_selenium_df['판매가'] = gmarket_selenium_df['판매가'].apply(extract_comma)


# In[23]:


import re

def extract_stars(x):
    ext = re.findall("\d+%", x)
    #데이터가 빈 경우가 있으므로 try, except문 사용
    try:
        stars = int(ext[0].replace('%', "")) #%를 제거한 뒤 int로 변환
    except:
        pass
    return stars if ext else None #데이터가 있을 경우 stars를 반환, 아닐 경우 None을 반환


# In[24]:


gmarket_selenium_df['만족도'] = gmarket_selenium_df['만족도'].apply(extract_stars)


# In[29]:


gmarket_selenium_df = gmarket_selenium_df.dropna().reset_index().iloc[:, 1:]


# In[30]:


gmarket_selenium_df.to_excel('gmarket_handfan_stars.xlsx')


# # 과제 (100점)

# #### 본인이 관심 있는 키워드에 대해서 해당 크롤링을 반복해서 수행하시오. 데이터를 수집하여 excel 파일로 저장하시오.

# In[4]:


#1. 필요한 라이브러리 import 하기 (10점)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


# In[5]:


#2. 본인이 관심 있는 키워드에 대해서 크롤링을 수행하고 상품명, 가격, 별점 정보 저장하기 (40점)
title_list = list()

# ChromeDriver의 경로를 지정하고, WebDriver 인스턴스를 생성합니다.
driver = webdriver.Chrome()

# 지마켓의 베스트 페이지를 엽니다.
driver.get('https://www.gmarket.co.kr/n/best?viewType=G&groupCode=G01')

# 상품명을 입력 받아 item_list 변수에 저장합니다.
item_list = driver.find_elements(By.CSS_SELECTOR, 'a.itemname')

for item in item_list:
    title_list.append(item.text)

driver.quit()


# In[6]:


print(title_list)


# In[7]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

title_list = list()
price_list = list()
star_list = list()

# ChromeDriver의 경로를 지정하고, WebDriver 인스턴스를 생성합니다.
driver = webdriver.Chrome()

# 지마켓의 메인 페이지를 엽니다.
driver.get('https://www.gmarket.co.kr')

# 검색어를 입력할 수 있는 input 요소를 찾습니다.
search_box = driver.find_element(By.NAME, 'keyword')

# 검색어를 입력하고, Enter 키를 눌러 검색을 실행합니다.
search_box.send_keys('원피스')
search_box.send_keys(Keys.RETURN)

# 결과 페이지가 로드될 때까지 잠시 기다립니다.
driver.implicitly_wait(3)

# 정보를 담은 박스를 선택합니다.
search_results = driver.find_elements(By.CSS_SELECTOR, 'div.box__information')

for result in search_results:
    #만족도가 없을 수도 있기에 try except문을 활용
    try:
        title_element = result.find_element(By.CSS_SELECTOR, 'span.text__item')
        price_element = result.find_element(By.CSS_SELECTOR, 'div.box__price-seller > strong')
        star_element = result.find_element(By.CSS_SELECTOR, 'span.image__awards-points > span')
        title_list.append(title_element.text)
        price_list.append(price_element.text)
        star_list.append(star_element.text)
    except:
        pass
    
# 작업이 끝나면 WebDriver를 종료하여 브라우저 창을 닫습니다.
driver.quit()


# In[9]:


#3. 적절히 데이터 전처리를 하여 DataFrame 객체로 만들고 Excel 파일로 저장하기 (50점)
#이때, DataFrame의 열은 "상품명, 판매가, 만족도"로 구성되어야 함.
import pandas as pd

gmarket_selenium_df = pd.DataFrame([title_list, price_list, star_list]).T


# In[10]:


gmarket_selenium_df.columns = ['상품명', '판매가', '만족도']


# In[11]:


gmarket_selenium_df


# In[12]:


def extract_comma(x):
    price = int(x.replace(",", "")) #replace로 쉼표까지 제거하고 int로 변환
    return price


# In[13]:


gmarket_selenium_df['판매가'] = gmarket_selenium_df['판매가'].apply(extract_comma)


# In[14]:


import re

def extract_stars(x):
    ext = re.findall("\d+%", x)
    #데이터가 빈 경우가 있으므로 try, except문 사용
    try:
        stars = int(ext[0].replace('%', "")) #%를 제거한 뒤 int로 변환
    except:
        pass
    return stars if ext else None #데이터가 있을 경우 stars를 반환, 아닐 경우 None을 반환


# In[15]:


gmarket_selenium_df['만족도'] = gmarket_selenium_df['만족도'].apply(extract_stars)


# In[16]:


gmarket_selenium_df = gmarket_selenium_df.dropna().reset_index().iloc[:, 1:]


# In[17]:


gmarket_selenium_df.to_excel('gmarket_handfan_stars.xlsx')


# In[ ]:




