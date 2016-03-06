#encoding=utf-8
from pymongo import MongoClient

import jieba
import json

def read_new_jokes:
    return []

def parse_word(sentence):
    words = jieba.cut(sentence, cut_all=False)
    for word in words:
        cursor = db.words.find({"word":word})
        if cursor.count() > 0:
            wds.update({"word":word}, {"$push":{"belong_to":title}})
            wds.update({"word":word}, {"$inc":{"freq":1}})
        else:
            insert_data_tmp = {"word":word, "freq":1, "belong_to":[title]}
            wds.insert(insert_data_tmp)
