#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 20:38:01 2021

@author: jyotisman
"""

'''
Need to create a file that takes four books of your choice from the
website books.toscrape.com and return the price information, the title, the 
category and the in-stock availability of each book.
'''

import scrapy
from scrapy_project.items import ScrapyProjectItem

class thirdSpider(scrapy.Spider):
    name = 'Books'
    # this is needed so that our crawler does not crawl through unallowed or unecessary pages
    #allowed_domains = [] 
    start_urls = [
        
        "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
        "http://books.toscrape.com/catalogue/the-requiem-red_995/index.html",
        "http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html",
        "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html",
        
        ]
    
    def parse(self, response):
        item = ScrapyProjectItem()
        
        item['title'] = response.xpath("//h1/text()").get()

        item['category'] = response.xpath('//*[@id="default"]/div/div/ul/li[3]/a/text()').get()
        
        #normalize-space gets rid of not just trailing and leading whitespaces but also extra spaces in between unlike unicode.strip
        item['in_stock'] = response.xpath('normalize-space(.//*[@id="content_inner"]/article/div[1]/div[2]/p[2])').get()
        
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        
        
        """
        # without using the xpaths from the inspects directly instead traversing the classes by looking at the html tree
        
        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        
        item['in_stock'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
        """
         
        return item    