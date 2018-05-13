
# coding: utf-8

# In[1]:


import torch
import numpy as np
from functools import reduce


# In[4]:


def nest_vector(vec1, vec2):
    return np.column_stack((vec1,vec2))


# In[5]:


def handle_index_list_return_matrix(word_to_ix,model,string):
    str_array = string.split()
    word_set = set(word_to_ix.keys())
    for str in str_array:
        if str not in word_set:
            str_array[str_array.index(str)] = '<unk>'
    #by using <unk> to embed out you dont know what might lead server problem for its large 
#value affects the final distance of matrix,test embed of <unk>
    index_set = [word_to_ix[str] for str in str_array]
    embed = model.embeddings
    vec_array = [embed(torch.tensor(index)).detach().numpy().reshape(-1,1) for index in index_set]
    mat = reduce(nest_vector,vec_array)
    return mat

