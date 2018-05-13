
# coding: utf-8

# In[13]:


import numpy
from pymongo import MongoClient
import pprint
import numpy as np
from handle_mat_compare import evaluate
from string_to_mat import main
from fy import fanyi
import sys
# In[14]:


#client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.pythondb
collection = db.python_collection
posts = db.posts


# In[21]:


def find_most__related_sentence(string):
    #mat_query = evaluate(string)
    temp_post = posts.find()[0]
    temp_value = evaluate(main(string),np.array(temp_post["mat"]))
    for post in posts.find():
        temp = evaluate(main(string),np.array(post["mat"]))
        if(temp  < temp_value):
            #print(temp_post["answear"])
            temp_post = post
            temp_value = temp
    return temp_post["answear"]

if __name__=="__main__":
    string_arr = sys.argv[1:]
    query_string=''
    for index in range(len(string_arr)):
        query_string+=' '
        query_string+=string_arr[index]
    query_string = query_string.strip()
    query_string = fanyi(query_string)
    #print(1)
    answear_string = fanyi(find_most__related_sentence(query_string))
    print(answear_string)
# In[30]:


#find_most__related_sentence("bro")

