import numpy
from pymongo import MongoClient
import pprint
import numpy as np
import string_to_mat
from fy import fanyi
#client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.pythondb
collection = db.python_collection
post = {}
posts = db.posts
while(1):
    question = input("key in the question:").strip()
    question = fanyi(question)
    print(question)
    answear = input("key in the answear:").strip()
    print(answear)
    answear = fanyi(answear)
    post["question"] = question
    post["answear"] = answear
    post["mat"] = string_to_mat.main(question).tolist()
    print(post["mat"])
    post_id = posts.insert_one(post).inserted_id
    print(post_id)
    