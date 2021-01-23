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
# Query generator for google search

for scrip in StockName:
    SearchQuery.append(scrip + " share BSE")

for eachSearchQuery in SearchQuery:
    print("each search query-->"+eachSearchQuery)
    for i in search(eachSearchQuery,  # The query you want to run
                    tld='com',  # The top level domain
                    lang='en',  # The language
                    num=10,  # Number of results per page
                    start=0,  # First result to retrieve
                    stop=1,  # Last result to retrieve
                    pause=2.0,  # Lapse between HTTP requests
                    ):
        BSEUrl = i
    print("BSE Url-->" + BSEUrl)
# print("url"+BSEUrl)
print("completed")
