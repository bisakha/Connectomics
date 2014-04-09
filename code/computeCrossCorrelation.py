#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.

from discretizeFluorescenceSignal import discretizeFluorescenceSignal
from myxcorr import myxcorr
from discretizeFluorescenceSignal import discretizeFluorescenceSignal
import numpy as np


def computeCrossCorrelation(F,debug):
    
### scores = computeCrossCorrelation(F)
### Baseline method to compute scores based on cross correlation measure 
### Cross correlation is normalized
### default value for timeLag is zero
### if other timeLag value is specified then crossCorrelation values are
### averaged for connection strength i->j as average
### crossCorrelation(-timeLag:0) and for j->i are averaged for
### crossCorrelation(0:timeLag)
    #F = discretizeFluorescenceSignal(F1)
    
#####compute cross correlation
    
    rows = F.shape[0]
    cols = F.shape[1]
    arr = []
    debug = True
    timeLag = 1
    #cols = 20
    for i in range(cols):
        #print 'i now '+str(i)
        for j in range(i+1,cols):
 
            crossCorr = myxcorr(F[:,i],F[:,j],timeLag);
            #print crossCorr[0:timeLag]
            Values_ij = np.mean(crossCorr[0:timeLag])
            
            Values_ji = np.mean(crossCorr[timeLag:2*timeLag])
            
            #if Values_ij == 0:
                #print 'Values_ij '+str(i)+' , '+ str(j)
            #if Values_ji == 0:
                #print 'Values_ji '+str(j)+' , '+ str(i)
            to_append = [i,j,Values_ij]
            arr.append(to_append)
            #print to_append
            to_append = [j,i,Values_ji]
            arr.append(to_append)
            #print to_append
        if debug:
            
            if (((float(i)/float(cols))*100)%10) == 0:
                print ('Percentage done : %d\n' %(((float(i)/float(cols))*100)))
    Matrix = [[0 for x in range(cols)] for x in range(cols)]


    for i in range(len(arr)):
            #print int(arr[i][0])
            #print int(arr[i][1])
            #print (arr[i][2])
            Matrix[int(arr[i][0])][int(arr[i][1])] = arr[i][2]
    #print Matrix
    print '*****************************************'
    #print np.array(Matrix)  
    #return np.array(Matrix)
    #return Matrix
    return np.array(Matrix)

