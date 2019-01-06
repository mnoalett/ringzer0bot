# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class Ringzer0BotPipeline(object):

    collection_name = 'scoreboard'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_SERVER'),
            mongo_db=crawler.settings.get('MONGODB_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if self.db[self.collection_name].find({'username': dict(item)['username']}).limit(1).count() > 0:
            self.db[self.collection_name].update_one({"username":dict(item)['username']}, {"$set": {'country':dict(item)['country'], 'member_since':dict(item)['member_since']}})
        else:
            self.db[self.collection_name].insert_one(dict(item))
        return item
