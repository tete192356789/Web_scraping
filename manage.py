from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv
import nltk
from nltk import sent_tokenize
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from testing import *

all_url = crawl('https://www.gamespot.com/')
a = game_spot_content(all_url)
df = pd.DataFrame.from_dict(a)

all_url2 = crawl('https://www.gameinformer.com/')
a2 = game_informer_content(all_url2)
df2 = pd.DataFrame.from_dict(a2)

all_url3 = crawl('https://www.gematsu.com/')
a3 = gematsu_content(all_url3)
df3 = pd.DataFrame.from_dict(a3)

all_url4 = crawl('https://www.techradar.com/')
a4 = techradar_content(all_url4)
df4 = pd.DataFrame.from_dict(a4)

all_url5 = crawl('https://n4g.com/')
a5 = n4g_content(all_url5)
df5 = pd.DataFrame.from_dict(a5)

all_url6 = crawl('https://www.mmorpg.com/')
a6 = mmorpg_content(all_url6)
df6 = pd.DataFrame.from_dict(a6)

sum_df = pd.concat([df, df2,df3,df4,df5,df6], axis=0,ignore_index = True)
print(sum_df)

sum_df.to_csv('content.csv')


data_from_csv = pd.read_csv('content.csv',encoding='utf-8')

pol_res = []
count_res = []
key_word = 'games'
for sen in data_from_csv['content']:

    clean_text = clean_text1(sen)
#     clean_text = sen.replace('\n','')
#     clean_text = clean_text.replace('/','')
#     clean_text = ''.join([c for c in clean_text if c != "'"])
    sentiment_pol = check_sentiment(clean_text)
    counter = count_keywords(clean_text,key_word)
    print(sentiment_pol)
    print('Word count :',counter)
    pol_res.append(sentiment_pol)
    count_res.append(counter)
data_from_csv['sentiment'] = pol_res
data_from_csv['count_word'] = count_res
# data_from_csv.to_csv('content_with_sentiment.csv', encoding='utf-8',index= False)
data_from_csv.to_csv('content_with_sentiment_count2.csv', encoding='utf-8',index= False)