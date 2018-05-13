
# coding: utf-8

# In[1]:


import pickle
from io import open
import sys, getopt
from router_vec_to_mat import handle_index_list_return_matrix
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F


# In[2]:


EMBEDDING_DIM,CONTEXT_SIZE = 10,2
f = open('word_to_ix.txt','rb')
word_to_ix = pickle.load(f)
f.close()


# In[3]:


class NGramLanguageModeler(nn.Module):

    def __init__(self, vocab_size, embedding_dim, context_size):
        super(NGramLanguageModeler, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(context_size * embedding_dim, 128)
        self.linear2 = nn.Linear(128, vocab_size)

    def forward(self, inputs):
        embeds = self.embeddings(inputs).view((1, -1))
        out = F.relu(self.linear1(embeds))
        out = self.linear2(out)
        log_probs = F.log_softmax(out, dim=1)
        return log_probs
model = NGramLanguageModeler(len(word_to_ix), EMBEDDING_DIM,CONTEXT_SIZE)
model.load_state_dict(torch.load('lm-model.pkl'))


# In[4]:


def main(argv):
    #string = ''
    #for index in range(len(argv)):
            #string+=' '
            #string+=argv[index]
    mat = handle_index_list_return_matrix(word_to_ix,model,argv)
    return mat
    print(mat)

#ain(sys.argv[1:])

