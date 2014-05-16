from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import WatchItem

class JomashopSpider(Spider):
    name = "jomashop"
    allowed_domains = ["www.jomashop.com"]
    start_urls = [
        "http://www.jomashop.com/omega-doorbuster-event.html?page=0&sf=1&sd=a"
    ]

    def parse(self, response):
        sel = Selector(response)
        names = sel.xpath("//div[@class='section-name']/b/a/text()")
        prices = sel.xpath("//div[@class='section-price']/b/text()")
        items = []
        ind = 0
        itemPrice = iter(prices)        
        for name in names:
            price = itemPrice.next()
            item = WatchItem()
            item['name'] = name.extract()
            item['price'] = price.extract()  
            items.append(item)
        return items