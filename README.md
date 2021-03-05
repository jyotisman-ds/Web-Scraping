# Web-Scraping
_Web scraping with Scrapy, BeautifulSoup and Selenium_

- [Overview](#overview)
- [Scrapy](#the-problem)
- [BeautifulSoup](#beautifulsoup)
- [Selenium (+ BeautifulSoup)](#selenium-(+-beautifulsoup))
- [Credits](#credits)


## Overview

This repo consists of some useful web scraping codes that I developed as part of some challenges in a web scraping course that I took in Udemy. The important python libraries explored in these codes are Scrapy, BeautifulSoup and Selenium.


## Scrapy

The code can be found [here](https://github.com/jyotisman-ds/Web-Scraping/blob/main/scrapy_project/scrapy_project/spiders/scrapy_challenge.py).

The important thing to note about scrapy is that it's a complete web crawling framework unlike BeautifulSoup which is mostly a parsing library. What it means is that scrapy first takes in the urls that you want to fetch and then it provides useful ways to parse contents in that webpage as well. You don't necessarily have to rely on other libraries.

```shell
scrapy crawl Books -o  scrapy_challenge.csv
```

![output](/scrapy_project/scrapy_project/spiders/scrapy_challenge.csv)
