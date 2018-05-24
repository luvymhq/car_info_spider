# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook


class CarInfoPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['CAR_BRAND', 'CAR_TYPE', 'CAR_SETTING', 'CAR_SUB_TYPE', 'CAR_PRICE'])

    def process_item(self, item, spider):
        line = [item['car_brand'], item['car_type'], item['car_setting'], item['car_sub_type'], item['car_price']]
        self.ws.append(line)
        self.wb.save('car_info.xlsx')
        return item