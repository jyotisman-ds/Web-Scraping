#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 01:34:52 2021

@author: jyotisman
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


def best_seller_amazon():
    
    url = "https://www.amazon.com/Best-Sellers/zgbs"
    headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Accept-Language':'en-US, en;q=0.5'})
    
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    # check connection status
    print(r.status_code)
    
    # count of reviews and the product name
    review_count_list = [i.text for i in soup.find_all('a', {'class' : 'a-size-small a-link-normal'})] 
    product_name = [name.text.strip().split('\n')[0] for name in soup.find_all("div",class_="a-section a-spacing-none p13n-asin")]

    # Putting them in a dataframe
    df = pd.DataFrame({'review_count' : review_count_list, 'product_name' : product_name})
    
    #print(review_count_list)
    #print(product_name)
    print(df)
    
    
    time.sleep(60)
    
# running once every minute
tot_time = time.time() + 2*60
while time.time()<tot_time:
    best_seller_amazon()
    
    
    
