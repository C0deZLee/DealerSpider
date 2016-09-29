#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from ..items import *

from scrapy.spiders import BaseSpider
from scrapy.selector import Selector

class DealerSpider(BaseSpider):
    name = "dealerspider"
    # all dealers
    start_urls = ["http://www.statecollege.com/auto/dealers/statecollegemotors-com,6547/",
                  "http://www.statecollege.com/auto/dealers/stocker-chevrolet,9803/",
                  "http://www.statecollege.com/auto/dealers/maggi-mitsubishi,16673/",
                  "http://www.statecollege.com/auto/dealers/state-college-ford--lincoln--inc-,25734/",
                  "http://www.statecollege.com/auto/dealers/sutliff-buick-gmc-cadillac,55999/",
                  "http://www.statecollege.com/auto/dealers/workman-auto--inc-,89034/",
                  "http://www.statecollege.com/auto/dealers/bobby-rahal-toyota,106275/",
                  "http://www.statecollege.com/auto/dealers/bobby-rahal-lexus,127161/",
                  "http://www.statecollege.com/auto/dealers/bobby-rahal-used-car-outlet,127170/",
                  "http://www.statecollege.com/auto/dealers/bobby-rahal-honda-of-state-college,187485/"]

    def parse(self, response):
        # all cars' url on current page
        for car_url in response.xpath('//a[@class="buttonV1"]/@href').extract():
            # go to detail page of car
            yield scrapy.Request(response.urljoin(car_url), callback=self.car_parse)

        #  next page
        if response.xpath('//div[@class="pager"][1]/a[last()]/text()').extract() != [] and response.xpath('//div[@class="pager"][1]/a[last()]/text()').extract()[0] == u'\u2192':
            next_page = str(response.xpath('//div[@class="pager"][1]/a[last()]/@href').extract()[0])
            yield scrapy.Request(next_page, callback=self.parse)

    def car_parse(self, response):
        '''Parse the html and get the data'''
        car_item = CarItem()
        car_item['DealerName'] = str(response.xpath('//*[@id="columnmiddle_wide"]/div[1]/div/div[1]/a[1]/text()').extract())[17:-1] # drop useless string
        car_item['DealerURL'] = str(response.xpath('//*[@id="columnmiddle_wide"]/div[1]/div/div[1]/a[2]/@href').extract()[0])
        car_item['DealerPhoneNum'] = str(response.xpath('//*[@id="columnmiddle_wide"]/div[1]/div/div[1]/div[2]/p[1]/text()').extract()[0])
        car_item['DealerAddress'] = str(response.xpath('//*[@id="columnmiddle_wide"]/div[1]/div/div[1]/div[2]/p[2]/text()').extract()[0][30:-1])+str(response.xpath('//*[@id="columnmiddle_wide"]/div[1]/div/div[1]/div[2]/p[2]/text()').extract()[1][17:-1])
        car_item['CarName'] = str(response.xpath('//*[@id="columnmiddle_wide"]/h1/text()').extract()[0])
        
        if response.xpath('//img[@id="image_large"]/@src').extract()!=[]:
            car_item['ImgURL'] = str(response.xpath('//img[@id="image_large"]/@src').extract()[0])
        else:
            car_item['ImgURL'] = ""
        if response.xpath('//b[@class="price"]/text()').extract()!=[]:
            car_item['Price'] = str(response.xpath('//b[@class="price"]/text()').extract()[0])
        else:
            car_item['Price'] = "Call / Email"
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[1]/td[2]/text()').extract()!=[]:
            car_item['Year'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[1]/td[2]/text()').extract()[0])
        else:
            car_item['Year'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[2]/td[2]/text()').extract()!=[]:
            car_item['New_Used'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[2]/td[2]/text()').extract()[0])
        else:
            car_item['New_Used'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[3]/td[2]/text()').extract()!=[]:
            car_item['Make'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[3]/td[2]/text()').extract()[0])
        else:
            car_item['Make'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[4]/td[2]/text()').extract()!=[]:
            car_item['Model'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[4]/td[2]/text()').extract()[0])
        else:
            car_item['Model'] =  ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[5]/td[2]/text()').extract()!=[]:
            car_item['Trim'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[5]/td[2]/text()').extract()[0])
        else:
            car_item['Trim'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[6]/td[2]/text()').extract()!=[]:
            car_item['Mile'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[6]/td[2]/text()').extract()[0])
        else:
            car_item['Mile'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[7]/td[2]/text()').extract()!=[]:
            car_item['Style'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[7]/td[2]/text()').extract()[0])
        else:
            car_item['Style'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[8]/td[2]/text()').extract()!=[]:
            car_item['Engine'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[8]/td[2]/text()').extract()[0])
        else:
            car_item['Engine'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[9]/td[2]/text()').extract()!=[]:
            car_item['Transmission'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[9]/td[2]/text()').extract()[0])
        else:
            car_item['Transmission'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[10]/td[2]/text()').extract()!=[]:
            car_item['ExColor'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[10]/td[2]/text()').extract()[0])
        else:
            car_item['ExColor'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[11]/td[2]/text()').extract()!=[]:
            car_item['InColor'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[11]/td[2]/text()').extract()[0])
        else:
            car_item['InColor'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[12]/td[2]/text()').extract()!=[]:
            car_item['VIN'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[12]/td[2]/text()').extract()[0])
        else:
            car_item['VIN'] = ""
        if response.xpath('//*[@class="auto_detail_data_table"]/tr[13]/td[2]/text()').extract()!=[]:
            car_item['StockNum'] = str(response.xpath('//*[@class="auto_detail_data_table"]/tr[13]/td[2]/text()').extract()[0])
        else:
            car_item['StockNum'] = ""
        if response.xpath('//div[@id="columnmiddle_wide"]/div[3]').extract()!=[]:
            car_item['Description'] = response.xpath('//div[@id="columnmiddle_wide"]/div[3]').extract()[0].encode('ascii','ignore')
        else:
            car_item['Description'] = ""

        yield car_item
