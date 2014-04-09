#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.



import numpy
import scipy
from sprand import _rand_sparse, sprand
from numpy import *
from scipy import sparse
import scipy.io as sio



def randomScore(F, arg):

    # Stupid method to compute scores assigning random values.
    density = 0.1
    n = F.shape[1]
    ij = numpy.random.randint(n, size=(2, n * n*density))
    data = numpy.random.rand(n * n *density)
    score = scipy.sparse.coo.coo_matrix((data, ij), (n, n))   
    return score
