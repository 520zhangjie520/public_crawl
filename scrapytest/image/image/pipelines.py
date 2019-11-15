# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from .spiders.img import headers
from scrapy.pipelines.images import  ImagesPipeline
class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        list1 = []
        try:
            for x in item.get(self.images_urls_field, []):
                list1.append(scrapy.Request(x,headers=headers))
        except:
            pass
        return list1