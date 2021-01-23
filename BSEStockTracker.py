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

StockName = ['TCS']#, 'WIPRO', 'INFOSYS']
SearchQuery = []
# Query generator for google search
GoogleSearchUrls=[]
BSEUrl=[]
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
        GoogleSearchUrls.append(Urls)
        print("URL---"+Urls)
        for singleUrl in GoogleSearchUrls:
            if BSEKeyword in singleUrl:
                BSEUrl.append(singleUrl)

                print("BSE Url-->" + singleUrl)
                break
        GoogleSearchUrls=[]

# print("url"+BSEUrl)
print("completed")
