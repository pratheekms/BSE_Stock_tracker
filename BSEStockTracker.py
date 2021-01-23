import time
start = time.time()
import bs4, requests
import openpyxl
import random
import logging
import urllib3
#from google import search

from googlesearch import search


print("hello world")

StockName='TCS'
BSEUrl=search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
