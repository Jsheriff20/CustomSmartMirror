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
driver = webdriver.Firefox("C:/Users/jacka/geckodriver-v0.27.0-win64/geckodriver.exe")
driver.get('https://moneypip.com/inx-live-charts/')

html = driver.page_source
soup = BeautifulSoup(html)

for tag in soup.find_all("span", class_="changePercent "):
    print(tag.text)