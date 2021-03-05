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

In the above code, all that we need to do is use our defined crawler ("Books") to crawl the urls defined in "start_urls" typing the following command in the terminal -

```shell
scrapy crawl Books -o  scrapy_challenge.csv
```
The output produced is a csv file which looks as follows -

|category|in_stock|price|title|
| --- | --- | --- | --- |
|Historical Fiction|In stock (20 available)|£53.74|Tipping the Velvet|
|Young Adult|In stock (19 available)|£22.65|The Requiem Red|
|Poetry|In stock (19 available)|£20.66|Shakespeare's Sonnets|
|Default|In stock (19 available)|£13.99|"Starving Hearts (Triangular Trade Trilogy, /#1)"|

The url used here is an artificially created website for the purposes of practicing your web scraping codes. It has a ton of different html, css or javascript elements to scrape.

## BeautifulSoup

The relevant code can be found [here](https://github.com/jyotisman-ds/Web-Scraping/blob/main/BS_challenge.py).

BeautifulSoup is sort of the go-to library for scraping web elements. The main advantage it provides as compared to let's say scrapy is its ability to adapt to changing websites.

We use the requests library in python to send the http requests. The idea then is to create a BeautifulSoup object and then use the several methods to access specific elements based on its type, class, etc.

We scrape a real website here, the Amazon [best sellers](https://github.com/jyotisman-ds/Web-Scraping/blob/main/BS_challenge.py) website. We scrape the product name and the total number of reviews for each product.

## Selenium (+ BeautifulSoup)

A combination of Selenium and BeautifulSoup is used in the [code](https://github.com/jyotisman-ds/Web-Scraping/blob/main/selenium_challenge.py) here to navigate to a page starting from a given url before scraping the contents of the final webpage.

Selenium is a library that automates browsers. It can go all the way from loading a browser to navigating through every clickable link and also taking care of pop-up windows.

We again scrape a real [website](https://sdsclub.com/). We go through several clickable links before finally scraping the required objects with BeautifulSoup. We make use of the 'DesiredCapabilities' method in the selenium library to disable the pop-ups in Chrome.

## Credits

Thanks to Udemy for hosting this interesting course on Modern [Web Scraping](https://www.udemy.com/course/modern-web-scraping-in-python/) and also to the creators/lecturers of the course for the wonderful content.
