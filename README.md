webScrapy1
==========

a simple web scraping script to download data from website

Overview
=========
In this project we use a tool called Scrapy to create the crawl to download the information we need from different website.

Scrapy is a fast high-level screen scraping and web crawling framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing. If you want to learn more about them you can go to http://scrapy.org/.

There are several spiders in this project:
1. dmoz_spider is a sample spider shows you how to use the scraping tool.
2. jomashop is a spider to download the watch prices from jomashop.com

Install the Scrapy:
-------------------
Open the terminal and input the following command: "install with: easy_install -U Scrapy or pip install Scrapy" or you may 
download the source file from http://scrapy.org/download/ and compile it yourself.

How to use scrapy:
===================

Creating a project:
--------------------
After you installed the Scrapy you can create a new project by a simple command just like Ruby on Rails.Input:

scrapy startproject tutorial

to your terminal and you can get the new project right now.

These are basically:

scrapy.cfg: the project configuration file
tutorial/: the project’s python module, you’ll later import your code from here.
tutorial/items.py: the project’s items file.
tutorial/pipelines.py: the project’s pipelines file.
tutorial/settings.py: the project’s settings file.
tutorial/spiders/: a directory where you’ll later put your spiders.

More detail about how to use this tool please visit http://doc.scrapy.org/en/latest/intro/tutorial.html.

Starting crwaling:
-------------------
After you finished the crawl we can get it started!

Input:

scrapy crawl YOURCRAWLNAME

and you can download whatever information you want from Internet!
