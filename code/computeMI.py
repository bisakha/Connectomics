
#http://stackoverflow.com/questions/20491028/optimal-way-
#for-calculating-columnwise-mutual-information-using-numpy



import numpy as np

from sklearn.metrics import mutual_info_score

from discretizeFluorescenceSignal import discretizeFluorescenceSignal

from jointEntropy import calc_MI

def computeMI(F, debug):
    D = discretizeFluorescenceSignal(F)
    bins = 5 
    n = D.shape[1]
    matMI = np.zeros((n, n))

    for ix in np.arange(n):
       for jx in np.arange(ix,n):
            matMI[ix,jx] = calc_MI(D[:,ix], D[:,jx], bins)
            matMI[jx,ix] = matMI[ix,jx]
    return matMI

