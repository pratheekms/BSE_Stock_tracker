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
SearchQuery=[]
# Query generator for google search

for i in StockName:
    SearchQuery.append(i + " share BSE")

for eachStock in SearchQuery:

query = 'TCS'
for i in search(query,  # The query you want to run
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
print(type(BSEUrl))
