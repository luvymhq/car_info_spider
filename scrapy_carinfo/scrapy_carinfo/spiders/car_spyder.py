# -*- coding: utf-8 -*-


import re
import string
import scrapy
from bs4 import BeautifulSoup as bs
from scrapy.http import Request
from scrapy_carinfo.items import CarinfoItem

class CarSpider(scrapy.Spider):
    name = 'carSpider'
    allowed_main_url = ['autohome.com.cn/grade/carhtml']
    bash_url = 'https://www.autohome.com.cn/grade/carhtml/'
    end_url = '.html'

    def start_requests(self):
        for i in 'A':  #string.ascii_uppercase:
            url = self.bash_url + i + self.end_url
            yield scrapy.Request(url,callback=self.get_name)
    #yield Request,请求Url,后面跟的是回调函数，你需要哪一个函数来处理这个url的返回值，就写这个函数在callback参数上

    def get_name(self, response):
        car_info_list = response.css('.rank-list-ul li h4')
        car_brand = response.css(".h3-tit::text").extract_first()
        # car_info_list = bs(response.text,'lxml').find_all('li')
        for car in car_info_list:
            car_info_url = 'https://www.autohome.com.cn/3170/#levelsource=000000000_0&pvareaid=101594'
            #'https:' + car.css("a::attr(href)").extract_first()
            #print(car_info_url)
            yield scrapy.Request(car_info_url, callback=self.get_car_detail,meta={'car_brand':car_brand,
                                                                                  'url':car_info_url})

    def get_car_detail(self, response):
        car_info_url = response.meta['url']
        car_brand = response.meta['car_brand']
        car_type = response.css(".tab-title a::text").extract_first()
        car_setting_list = response.css(".interval01-list-cars-text::text").extract()
        car_catalog = response.css(".interval01-list")  # 找出有多少个分类
        for i in range(len(car_catalog)):
            car_sub_type_list = car_catalog[i].css(".interval01-list-cars-infor p a::text").extract()
            car_price_list = car_catalog[i].css(".interval01-list-guidance div::text").extract()
            car_price_list_new = [price.strip() for price in car_price_list if price.strip() != '']  # 去掉回车和换行
            car_setting = car_setting_list[i]
            for k in range(len(car_sub_type_list)):
                car_sub_type = car_sub_type_list[k]
                car_price = car_price_list_new[k]
                # print(car_brand+car_type+car_setting+car_sub_type + car_price)
                yield scrapy.Request(car_info_url, callback=self.get_car_detail_1, meta={'car_brand': car_brand,
                                                                                         'car_type': car_type,
                                                                                         'car_setting': car_setting,
                                                                                         'car_sub_type': car_sub_type,
                                                                                         'car_price': car_price})

    def get_car_detail_1(self, response):
        print(response.meta)
        # carInfoItem = CarinfoItem()
        # carInfoItem['car_brand'] =response.meta['car_brand']
        # carInfoItem['car_type'] = response.meta['car_type']
        # carInfoItem['car_setting'] = response.meta['car_setting']
        # carInfoItem['car_sub_type'] = response.meta['car_sub_type']
        # carInfoItem['car_price'] = response.meta['car_price']
        # yield carInfoItem




