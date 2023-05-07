import requests
import bs4
import lxml
import re
from collections import namedtuple

#for scraping latest news
from datetime import time,date,timedelta
#working for today and yesterday

#time structure
today = date.today()
yesterday = today - timedelta(days = 1)

today = today.strftime("%Y/%m/%d")
yesterday = yesterday.strftime("%Y/%m/%d")

#key words for scraping
key_words = ['Russia','war ','nuclear ','Putin ','killed ','rocket','Duma','Poland','Polish ','Duda ','Zelenski','Rada']

#structure of scraping data
Article = namedtuple("Article", "title link")

#CNN

def cnn(link):
    articles_world = []
    articles_europe = []
    
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.content,'html.parser')
    
                  
    for element in soup.find_all('a',class_="container__link container_lead-plus-headlines__link"):
              
        for key_word in key_words:
            if key_word in element.text and (str(today) in element['href'] or str(yesterday) in element['href']):                 
                articles_world.append(
                    Article(
                            title=element.text.replace('\n', '').replace('\xa0','').strip(),
                            link='https://edition.cnn.com'+element['href']
                    )
                )  
                 

    for element in soup.find_all('a',class_="container__link container_lead-plus-headlines-with-images__link"):
            
        for key_word in key_words:
            if key_word in element.text and (str(today) in element['href'] or str(yesterday) in element['href']):                 
                articles_europe.append(
                    Article(
                            title=element.text.replace('\n', '').replace('\xa0','').strip(),
                            link='https://edition.cnn.com'+element['href']
                    )
                ) 
            
    
    
    articles = articles_world + articles_europe

    return articles

#BBC

def bbc(link):

    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.content,'html.parser')

    articles = []

    for element in soup.find_all('a',class_="qa-heading-link lx-stream-post__header-link"):
        for key_word in key_words:
             if key_word in element.text:
                articles.append(
                        Article(
                                title=element.text,
                                link='https://www.bbc.com'+element['href']
                        )
                )

    return list(set(articles))

#MEDUZA

def meduza(link):
    articles = []
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.content,'html.parser')
    
           
    for element in soup.find_all('a',class_="Link-root Link-isInBlockTitle"):
            
            for key_word in key_words:
                if key_word in element.text and (str(today) in element['href'] or str(yesterday) in element['href']):                 
                    articles.append(
                        Article(
                                title=element.text,
                                link='https://meduza.io' + element['href']
                        )
                    )
    return articles
                    
    

    
                  
                
    