from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_req(url):
    return requests.get(url).text
def get_soup(req):
    return BeautifulSoup(req,'html.parser')
def crawler(url,c):
    l = []
    
    def crawl6(url,c):
        
        req = get_req(url)
        soup = get_soup(req)
        if c > 0 :
            for i in soup.find_all('a'):

                try:
                    if i['href'].startswith('/'):
                        link = urljoin(url,i['href'])

                        if link not in l:
                            l.append(link)
                            crawl6(link,c-1)
                        else:
                            pass
                    elif i['href'].startswith('h'):
                        link = i['href']
                        if link not in l:
                            l.append(link)
                            crawl6(link,c-1)
                        else:
                            pass
                    else:
                        pass
        #             l = l + l2
                except:
                    pass
        
    
    crawl6(url,c)
    return l
   
a = crawler('https://www.gamespot.com/',3)

print(len(a))