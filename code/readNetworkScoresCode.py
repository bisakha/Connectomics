#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.


import numpy as np
import scipy

from numpy import *
from scipy import sparse
import scipy.io as sio




def readNetworkScores(filename):

#% Read the network architecture from the original format as a spase nxn matrix, 
#% whose (i,j)th entry indicates neuron i is connected to neuron j 
#% with a certain strength.
#% N is the dimension of the scores matrix....if it is not specified it will
#% be inferred.

    l = []
   
    with open(filename, 'r') as f:
     for line in f:
      line = line.strip()
      if len(line) > 0:
        l.append(map(int, line.split(',')))
     l1 = loadtxt(filename,delimiter=",")    
   #% Keep only 0/1 weights, ignore blocked connections
    Matrix = [[0 for x in xrange(int(l1.max()))] for x in xrange(int(l1.max()))]

    for i in range(0,len(l1)-1):
        if l1[i][2] > 0:
            l1[i][2] = 1
            
            Matrix[int(l1[i][0])-1][int(l1[i][1])-1] = 1
            
        if l1[i][2] <= 0:
            l1[i][2] = 0
            
            Matrix[int(l1[i][0])-1][int(l1[i][1])-1] = 0
            
            
    N = len(l1)

    #scores = np.matrix(Matrix)
    scores = Matrix
    #scores = scipy.sparse.coo.coo_matrix(l[:,0], l[:,1], l[:,2], (N, N));
    return scores





