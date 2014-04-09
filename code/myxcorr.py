###    function crossCorr = myxcorr(x,y,timeLag)
###    function to compute cross correlation between two time series




from multmat import matrixmult
import math
from copy import copy, deepcopy
from numpy import *
import numpy

def myxcorr(x1,y1,timeLag):
       
       crossCorr = []
       index = 0;
      
       
       #x = ((numpy.array(x1))[numpy.newaxis])
       #y = ((numpy.array(y1))[numpy.newaxis])
       x = ((numpy.array(x1))[numpy.newaxis])
       y = ((numpy.array(y1))[numpy.newaxis])
       #print x
       #print y
       n = x.shape[1];
       
       for i in range(-timeLag-1,0,1):
            j = -i

            #print 'y[:,j:n] '+str(y[:,j-1:n])
            #print 'x[:,0:n-j] '+str(x[:,0:n-j+1])
            sum = matrixmult(y[:,j-1:n], x[:,0:n-j+1])
            #print str(1)
            crossCorr.append(sum)
            #print crossCorr


       for i in range(0,timeLag,1):
 
           sum = matrixmult(x[:,i:n],y[:,0:n-i])
           #print str(2)
           #print 'x[:,i+1:n] '+str(x[:,i+1:n])
           #print 'y[:,0:n-i-1] '+str(y[:,0:n-i-1])
           crossCorr.append(sum)
           #print crossCorr
 
       crossCorr_array = numpy.asarray(crossCorr)
       x_sum = matrixmult(x,x)
       #print math.sqrt(x_sum)
       final_result = crossCorr_array/math.sqrt(x_sum)
       #print final_result
       y_sum = matrixmult(y,y) 
       #print math.sqrt(y_sum)      
       final_result_1 = final_result/math.sqrt(y_sum)
       #print final_result_1
       return final_result_1
 
#### normalize crossCorrelation
#crossCorr = crossCorr/sqrt(x'*x)/sqrt(y'*y);
