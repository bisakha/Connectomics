#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.

from discretizeFluorescenceSignal import discretizeFluorescenceSignal
from myxcorr import myxcorr
#from discretizeFluorescenceSignal import discretizeFluorescenceSignal
import numpy as np
import scipy
from scipy.stats.stats import pearsonr

def computePearsonsCorrelation(F,debug):
    
### scores = computeCrossCorrelation(F)
### Baseline method to compute scores based on cross correlation measure 
### Cross correlation is normalized
### default value for timeLag is zero
### if other timeLag value is specified then crossCorrelation values are
### averaged for connection strength i->j as average
### crossCorrelation(-timeLag:0) and for j->i are averaged for
### crossCorrelation(0:timeLag)
    F1 = discretizeFluorescenceSignal(F)
    
    
#####compute cross correlation

    #F1 = F
    #return np.corrcoef(F,  y=None, rowvar=0, bias=0, ddof=None)
    M = np.corrcoef(F1.T )
    #M = np.corrcoef(F1, bias = 0,rowvar=0)
    #M = scipy.corrcoef(F1,rowvar = 0)
    #np.correlate(F, F, mode='same')
    np.fill_diagonal(M, 0)
    
    return M
