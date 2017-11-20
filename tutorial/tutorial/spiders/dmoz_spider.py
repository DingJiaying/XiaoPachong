# -*- coding: cp936 -*
import scrapy
 
from tutorial.items import DmozItem
 
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.python.org/downloads/",
        "https://www.python.org/community/"
    ]
 
    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
 
        return items
   
