##http://orange.biolab.si/blog/2012/06/15/joint-entropy-in-python/

import numpy as np

def entropy(X1):
    [rows, cols] = X1.shape
    entropies = np.zeros(shape=(cols,1))
    for i in range(cols):
        X = X1[:,i] 
        probs = [np.mean(X == c) for c in set(X)]
        entropies[i] = np.sum(-p * np.log2(p) for p in probs)
    #print entropies
    return entropies

