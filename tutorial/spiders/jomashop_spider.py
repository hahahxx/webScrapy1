from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from tutorial.items import WatchItem

class JomashopSpider(Spider):
    name = "jomashop"
    allowed_domains = ["www.jomashop.com"]
    start_urls = [
        "http://www.jomashop.com"
    ]

    def parse(self, response):
        sel = Selector(response)
        brands = sel.xpath("//div[@class='aumscrollnav']//div[@class='newaumleftclapnav_menu-2']/a")
        #prices = sel.xpath('//div[@class='section-price']')       
        req = []
        for brand in brands:
            brandLink = brand.xpath('@href').extract()
            brandName = brand.xpath('text()').extract()
            newBrandLink = "http://www.jomashop.com/" + brandLink[0]
            print  brandLink[0]
            r = Request(newBrandLink, callback=self.parse_brand)
            req.append(r)
        #subbrand = sel.xpath("//div[@class = 'section-browse']")
        #return items
        return req

    def parse_brand(self, response):
        sel = Selector(response)
        ifSubBrand = sel.xpath("//div[@class='section-browse']")
        subBrands = sel.xpath("//div[@class='section-name']/b/a/@href")
        branditems = []
        req = []
        if len(ifSubBrand):
            for subBrand in subBrands:
                branditem = WatchItem()
                subBrandLink = subBrand.extract()
                newSubBrandLink = "http://www.jomashop.com/" + subBrandLink
                print newSubBrandLink
                branditems.append(branditem)
                r = Request(newSubBrandLink, callback=self.parse_price)
                req.append(r)
        else:
            print 'xxxxxxxxxxxxxxxxxxxxxxxxxxbrandNamebrandNamebrandNamebrandName'
        return req
        

    def parse_price(self,response):
        sel = Selector(response)
        names = sel.xpath("//div[@class='section-name']/b/a/text()")
        picUrls = sel.xpath("//table//table/tr/td//a/img/@src")
        prices = sel.xpath("//div[@class='section-price']/b/text()")
        items = []
        itemPrice = iter(prices)   
        picUrl = iter(picUrls)  
        for name in names:
            picIter = picUrl.next().extract()
            price = itemPrice.next().extract().replace('$','').replace(',','')
            print price
            item = WatchItem()
            item['name'] = name.extract()
            item['price'] = price  
            item['imgUrl'] = picIter
            items.append(item)
        return items
