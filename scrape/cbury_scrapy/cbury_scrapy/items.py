# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CburyItem(scrapy.Item):
    da_no = scrapy.Field()
    date_lodged = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    date_lodged = scrapy.Field()
    est_cost = scrapy.Field()
    status = scrapy.Field()
