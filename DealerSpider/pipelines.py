# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import re

class CarPipeline(object):
    def process_item(self, item, spider):
        # use re to remove html tags in description
        # from http://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
        cleanr =re.compile('<.*?>')
        item['Description'] = re.sub(cleanr,'', item['Description'])
        # connect redis
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        # increase id
        next_car_num = r.incr('next_car_num')
        # get value list
        input_value_list = {
            'ImgURL' : item['ImgURL'],
            'Price' : item['Price'],
            'Year' : item['Year'],
            'New_Used' : item['New_Used'],
            'Make' : item['Make'],
            'Trim' : item['Trim'],
            'Mile' : item['Mile'],
            'Model' : item['Model'],
            'Style' : item['Style'],
            'Engine' : item['Engine'],
            'Transmission' : item['Transmission'],
            'ExColor' : item['ExColor'],
            'InColor' : item['InColor'],
            'VIN' : item['VIN'],
            'StockNum' : item['StockNum'],
            'Description' : item['Description'],
            'DealerName' : item['DealerName'],
            'DealerURL' : item['DealerURL'],
            'DealerAddress' : item['DealerAddress'],
            'DealerPhoneNum' : item['DealerPhoneNum']
        }
        # save to database
        r.hmset('car:'+str(next_car_num), input_value_list)
        return item
