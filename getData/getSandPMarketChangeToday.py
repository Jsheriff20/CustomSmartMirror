import requests
import sys
from bs4 import BeautifulSoup

# def getFormsXmlFromEdgar(companyTicker):
#
#     #get the data from the page an return it for data extraction
#     result = requests.get("https://moneypip.com/inx-live-charts/")
#     src = result.content
#     soup = BeautifulSoup(src, 'lxml')
#
#     print(soup.find_all("span"))
#
#     return soup
#
# getFormsXmlFromEdgar("ad")

from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox(executable_path="C:\\Users\\jacka\\geckodriver-v0.27.0-win64\\geckodriver.exe")
driver.get('https://moneypip.com/inx-live-charts/')

soup = BeautifulSoup(driver.page_source, features="lxml")

# for tag in soup.find_all("span", {"class": "changePercent"}):
for tag in soup.find_all("span"):
    print(tag.text)