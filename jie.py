#encoding=utf-8
import jieba
import json
from pymongo import MongoClient


client = MongoClient()
db = client.joke
wds = db.words

with open('joke.dat') as jokes:
    for joke in jokes:
        js = json.loads(joke)
        print js['title']
        title = js['title']
        words = jieba.cut(js['content'], cut_all=False)
        for word in words:
            cursor = db.words.find({"word":word})
            if cursor.count() > 0:
                wds.update({"word":word}, {"$push":{"belong_to":title}})
                wds.update({"word":word}, {"$inc":{"freq":1}})
            else:
                insert_data_tmp = {"word":word, "freq":1, "belong_to":[title]}
                wds.insert(insert_data_tmp)
