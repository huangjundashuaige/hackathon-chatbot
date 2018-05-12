
# coding: utf-8

# In[16]:


from fy import fanyi
from functools import reduce


# In[17]:


def nest_str_array(str1,str2):
    str1+=' '
    str1+=str2
    return str1


# In[37]:


def translate(be_translated):
    string = fanyi(be_translated)
    str_array = string.split('\'')
    str_array = reduce(nest_str_array,str_array)
    str_array = str_array.split(',')
    str_array = reduce(nest_str_array,str_array)
    str_array = str_array.split('.')
    str_array = reduce(nest_str_array,str_array)
    str_array = str_array.split()
    filter(lambda x: x!='',str_array)
    for index in range(len(str_array)):
        str_array[index]=str_array[index].lower()
        if(str_array[index] == 'm'):
            str_array[index] = 'am'
        elif(str_array[index]=='re'):
            str_array[index]='are'
        elif(str_array[index]=='s'):
            str_array[index]='is'
    return str_array


# In[38]:


#print(translate('你好我很好'))

