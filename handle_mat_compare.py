
# coding: utf-8

# In[3]:


import torch
import numpy as np
from math import sqrt

# In[13]:


def evaluate(mat1,mat2):
    mat2 = np.array(mat2[:mat1.shape[0],:mat1.shape[1]])
    mat3 = mat1.transpose().dot(mat2)
    mat4 = mat3.transpose().dot(mat3)
    mat1_det = mat1.transpose().dot(mat1)
    mat2_det = mat2.transpose().dot(mat2)
    mat1_det_ = np.linalg.det(mat1_det)
    mat2_det_ = np.linalg.det(mat2_det)
    #print((mat1_det*mat2_det))
    #return np.linalg.det(mat4)/(mat1_det*mat2_det)
    mat1_norm = np.linalg.norm(mat1_det)
    mat2_norm = np.linalg.norm(mat2_det)
    mat4_norm = np.linalg.norm(mat4)
    #result=mat4_norm/(mat1_norm*mat2_norm)
    result= mat4_norm/(mat1_norm*mat2_norm)+mat4.shape[0]/5
    #print(result)
    return result

# In[14]:




