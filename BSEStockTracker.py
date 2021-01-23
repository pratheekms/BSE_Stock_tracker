import time

start = time.time()
import bs4, requests
import openpyxl
import random
import logging
import urllib3
# from google import search

from googlesearch import search

print("hello world")

StockName = ['TCS', 'WIPRO', 'INFOSYS']
SearchQuery = []
BSEUrlsDict={}
ScripCount=1
# Query generator for google search
GoogleSearchUrls = []
BSEUrl = []
for scrip in StockName:
    eachSearchQuery = scrip + " share price from BSEindia"

    # for eachSearchQuery in SearchQuery:
    print("each search query-->" + eachSearchQuery)
    for Urls in search(eachSearchQuery,  # The query you want to run
                       tld='com',  # The top level domain
                       lang='en',  # The language
                       num=10,  # Number of results per page
                       start=0,  # First result to retrieve
                       stop=5,  # Last result to retrieve
                       pause=2.0,  # Lapse between HTTP requests
                       ):
        BSEKeyword = 'bseindia'
        # GoogleSearchUrls.append(Urls)
        #print("URL---" + Urls)
        singleUrl=Urls
        # for singleUrl in GoogleSearchUrls:
        if BSEKeyword in singleUrl:
            BSEUrl.append(singleUrl)
            BSEUrlsDict.update({ScripCount: {'name': scrip, 'URL': singleUrl}})
            print("BSE Url-->" + singleUrl)
            ScripCount += 1
            break
        GoogleSearchUrls = []


headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
#url="https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
urllib3.disable_warnings()
for scrapingUrl in BSEUrl:
    res=requests.get(scrapingUrl,verify=False,headers=headers)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,"html.parser")            #'lxml')
    ochl = soup.find_all("div", {"class": "whitebox"})
    print(ochl)
# print("url"+BSEUrl)
print("completed")
