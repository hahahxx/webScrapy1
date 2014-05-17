from scrapy.spider import Spider
from scrapy.selector import Selector
import psycopg2 
from datetime import date
from tutorial.items import WatchItem

class JomashopSpider(Spider):
    
    name = "jomashop"
    allowed_domains = ["www.jomashop.com"]
    start_urls = [
        "http://www.jomashop.com/omega-constellation-watches.html?page=0&sf=1&sd=a"
    ]

    def parse(self, response):
        conn = psycopg2.connect(database="watches",user="yigao",password="secret",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        sel = Selector(response)
        names = sel.xpath("//div[@class='section-name']/b/a/text()")
        picUrls = sel.xpath("//table//table/tr/td//a/img/@src")
        prices = sel.xpath("//div[@class='section-price']/b/text()")
        items = []
        itemPrice = iter(prices)   
        picUrl = iter(picUrls)  
        
        for name in names:
            conn = psycopg2.connect(database="watches",user="yigao",password="secret",host="127.0.0.1",port="5432")
            cur = conn.cursor()
            picIter = picUrl.next().extract()
            price = itemPrice.next().extract().replace('$','').replace(',','')
            cur.execute("INSERT INTO watches (PRICE,NAME,IMGLINK,CREATED_AT) VALUES (\
                %d, \'%s\', \'%s\', \'%s\')" %(float(price), name.extract(), picIter, date.today().isoformat() ));
            item = WatchItem()
            item['name'] = name.extract()
            item['price'] = price  
            item['imgUrl'] = picIter
            items.append(item)
            conn.commit();
        return items