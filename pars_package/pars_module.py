
#working for today and yesterday

import requests
from bs4 import BeautifulSoup
import lxml
import re
from collections import namedtuple

#for scraping latest news
from datetime import time,date,timedelta
from time import strftime

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
