
# coding: utf-8

# In[1]:

import pickle
from sklearn.metrics import adjusted_rand_score

with open("truth.pickle","rb") as f:
    truth = pickle.load(f)
    
def rand_index(clusters):
    elems = list(set.union(*truth))

    # Index of Containing Set
    memory_truth = {}
    memory_clusters = {}
    def ics(element, set_list, set_list_name):
        if set_list_name == "truth":
            if element in memory_truth:
                return memory_truth[element]
        if set_list_name == "clusters":
            if element in memory_clusters:
                return memory_clusters[element]

        for c, s in enumerate(set_list):
            if element in s:
                if set_list_name == "truth":
                    memory_truth[element] = c
                if set_list_name == "clusters":
                    memory_clusters[element] = c
                return c

    x = [ics(e, clusters, 'clusters') for e in elems]
    y = [ics(e, truth, 'truth') for e in elems]
    return adjusted_rand_score(x,y)

