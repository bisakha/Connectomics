import numpy 

from discretizeFluorescenceSignal import discretizeFluorescenceSignal
from entropy import entropy

##% Baseline method to compute scores based on 
##% Information Geometry Causal Inference,
##% Inspired by:
##% [1]  P. DaniuÅ¡is, D. Janzing, J. Mooij, J. Zscheischler, B. Steudel,
##%      K. Zhang, B. SchÃ¶lkopf:  Inferring deterministic causal relations.
##%      Proceedings of the 26th Annual Conference on Uncertainty in Artificial 
##%      Intelligence (UAI-2010).  
##%      http://event.cwi.nl/uai2010/papers/UAI2010_0121.pdf
##% It boils down to computing the difference in entropy between pairs of
##% variables:
##% scores(i, j) = H(j) - H(i)

##%==========================================================================
##% Package: ChaLearn Connectomics Challenge Sample Code
##% Source: http://connectomics.chalearn.org
##% Author: Bisakha Ray
##% Date: April 2014
##% Last modified: NA
##% Contact: causality@chalearn.org
##% License: GPL v3 see http://www.gnu.org/licenses/
##%==========================================================================
def computeIGCI(F, debug):    
    
 
###    %% Discretize the fluorescence signal
    D = discretizeFluorescenceSignal(F)
    
###     %% Compute the entropy

    H = entropy(D)

#####    %% Compute the scores as entropy differences (vectorized :-))

 
    n = len(H)

    scores = numpy.zeros(shape=(n,n))

    #scores = numpy.vstack([scores, H.T[0]])
    for i in range(n):
        scores[i] = H.T[0]
    scores = scores - scores.T

    #print scores    
    return scores
