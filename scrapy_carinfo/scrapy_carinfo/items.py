# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_brand = scrapy.Field()
    car_type = scrapy.Field()
    car_setting = scrapy.Field()
    car_sub_type = scrapy.Field()
    car_price = scrapy.Field()

    pass
