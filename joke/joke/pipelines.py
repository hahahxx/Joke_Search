# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient

class JokePipeline(object):
    def __init__(self):
        self.file = open('joke.dat', 'wb')
        self.client = MongoClient()
    def process_item(self, item, spider):
        #val = "\t{0}t\{1}\n".format(item['title'], item['content'])
        #self.file.write( val )
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        db = self.client.joke
        jks = db.joke_table
        insert_data_tmp = {"content":item['content'], "title":item['title'],
            "state":"new"}
        jks.insert(insert_data_tmp)
        self.file.write(line)
        return item
