# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CarItem(scrapy.Item):
    """Definition of CarItem."""
    ImgURL = scrapy.Field()
    Price = scrapy.Field()
    Year = scrapy.Field()
    New_Used = scrapy.Field()
    Make = scrapy.Field()
    Trim = scrapy.Field()
    Mile = scrapy.Field()
    Model = scrapy.Field()
    Style = scrapy.Field()
    Engine = scrapy.Field()
    Transmission = scrapy.Field()
    ExColor = scrapy.Field()
    InColor = scrapy.Field()
    VIN = scrapy.Field()
    StockNum = scrapy.Field()
    Description = scrapy.Field()
    DealerName = scrapy.Field()
    DealerURL = scrapy.Field()
    DealerAddress = scrapy.Field()
    DealerPhoneNum = scrapy.Field()
