from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd
all_url = []

def get_req(url):
    return requests.get(url).text
def get_soup(req):
    return BeautifulSoup(req,'html.parser')
       

def crawl(url,i):
    
    req = get_req(url)
    soup = get_soup(req)
    if i >0:  
        for i in soup.find_all('a'):
        
            try:
                if i['href'].startswith('/'):
                    link = urljoin(url,i.get('href'))
                    all_url.append(link)
                
                elif i['href'].startswith('h'):
                    link = i.get('href')
                    all_url.append(link)
            
                
            except:
                pass
    else:
        return 0
crawl('https://www.gamespot.com/',3)
print(all_url)
print(len(all_url))

def count_words(url, keyword):
    r = requests.get(url, allow_redirects=False)
    count =  r.text.count(keyword)
    return count

data = []
key = 'games'
for url in all_url:
    obj = {}
    obj['url'] = url
    obj['count'] = count_words(url,key)
    data.append(obj)

df = pd.DataFrame(data)
print(df)


# key = 'games'
# url_list = ['https://www.gamespot.com/','https://www.pcgamer.com/news/','https://kotaku.com/','https://gamerant.com/'
#             ,'https://www.gameinformer.com/','https://www.ign.com/','https://www.thegamer.com/','https://www.theverge.com/games','https://www.gematsu.com/'
#             ,'https://www.techradar.com/gaming/news','https://www.rockpapershotgun.com/news','https://n4g.com/','https://www.online-station.net/'
#             ,'https://screenrant.com/gaming/','https://www.gamesradar.com/news/','https://www.bgr.in/category/gaming/','https://www.msn.com/en-us/entertainment/gaming'
#             ,'https://www.mmorpg.com/','https://www.pocket-lint.com/games/news','https://store.steampowered.com/news/']
# data = []
# for i in url_list:
#     d={}
#     res = count_words(i,key)
#     if 'www.' in i:
#         d['name'] = i.replace('https://www.',"").split('.')[0]
#     else:
#         d['name'] = i.replace('https://',"").split('.')[0]
#     d['url'] = i
#     d['total_key'] = res
#     data.append(d)

# df =pd.DataFrame.from_dict(data)
# print(df)