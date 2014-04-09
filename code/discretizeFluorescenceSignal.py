#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.


import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy

def discretizeFluorescenceSignal(F):

# DISCRETIZEFLUORESCENCESIGNAL discretizes the fluorescence signal so it
# can be used to compute the joint PDF. If conditioning is applied, the
# entries above the conditioning level are returned in the G vector.
#
# USAGE:
#    D = discretizeFluorescenceSignal(F)
#
# INPUT arguments:
#    F - Fluorescence data (each row a sample, each column a neuron).
#
# INPUT optional arguments ('key' followed by its value): 
#    'bins' - Number of bins to use in the discretization (before
#    conditioning). If the entry is a vector, it will define the bin edges
#    (default 3).
#
#   'relativeBins' - (true/false). If true the bins are defined based on
#    the min and max values of each sample. If false, they are defined
#    based on the absolute limits (default false).
#
#    'conditioningLevel' - Value used for conditioning. If the
#    value is 0 the level is guessed (for now, the peak of the histogram
#    plus 0.05). Set it to inf to avoid conditioning (default 0).
#
#   'highPassFilter' - (true/false). Apply a high pass filter to the
#   fluorescence signal, i.e., work with the derivative (default true).
#
#    'debug' - true/false. Show additional partial information (default
#    false).
#
#  
# OUTPUT arguments:
#    D - The discretized signal (each row a sample, aech column a neuron).
#
#    G - Vector defining the global conditioning level of the signal at
#    that given time (for now 1 and 2 for below and above the level).
#
# EXAMPLE:
#    D = discretizeFluorescenceSignal(F, 'bins', 3, 'debug', true);
#
#    (Stetter 2013) Stetter, O., Battaglia, D., Soriano, J. & Geisel, T. 
#    Model-free reconstruction of excitatory neuronal connectivity from 
#    calcium imaging signals. PLoS Comput Biol 8, e1002653 (2012).

### Assign defuault values
        
    relativeBins = False;                           
    #conditioningLevel = 0.25; #Old default = 0
    conditioningLevel = 0.12
    debug = True;                           
    highPassFilter = True;                          
                                
                                
    epsilon = 1e-3; # To avoid weird effects at bin edges                           
                                
    #Get the conditioning level                         
    avgF = np.mean(F, axis = 1, dtype=np.float64)                           
    if(conditioningLevel == 0):                         
        #hits,pos,patches = np.histogram(avgF, bins = 100);                         
        hits = np.histogram(avgF,  100);                            
        idx = np.argmax(hits[0])                            
        pos = hits[1]                           
        CL =  pos[idx]+0.05;                            
        print('Best guess for conditioning found at: % .2f \n'%(CL));                           
    else:                           
        CL = conditioningLevel;                         
                                
    #print avgF                           
    ###Apply the conditioning                           
    G = []  
    for i in range(len(avgF)):                          
       if avgF[i] >= CL :                           
           G.append(2)                          
       else:                            
           G.append(1)                          
                            
    #hist, bins = np.histogram(F, bins=100)
    hist, bins = np.histogram(F, bins = 100)    
    width = 0.7 * (bins[1] - bins[0])                           
    center = (bins[:-1] + bins[1:]) / 2                         
    plt.bar(center, hist, align='center', width=width)                          
    #plt.show()                          
                                
    ###Apply the high pass filter                           
    F_min = np.amin(F, axis=0)                          
    F_max = np.amax(F, axis=0)                          
    diff_F = []                         
    diff_F = np.diff(F.T)                         
    #print np.amin(diff_F, axis=0)                           
    #print np.amax(diff_F, axis=0)                           
    #F = np.diff(F)                         
                                
    G = G[1:len(G)-1]                           
    binEdges = []                           
                                
    ### Discretize the signal
    F = deepcopy(diff_F)
    D = deepcopy(F)                         
    D[:] = np.NAN                           
    if(len(bins) > 1):                          
       relativeBins = False; # Just in case                         
                                
    F_min = np.amin(diff_F, axis=0)                         
    F_max = np.amax(diff_F, axis=0)                         
    #print F_min                         
    #print diff_F.min()                          
    #print F_max                         
    #print diff_F.max()                          
    #print diff_F.shape[0]                           
    #print diff_F.shape[1]                           
    #print len(diff_F)                           
    #print F_min.shape[0]                            
    hits = []                           
    bins = [3]
    #bins = [-10,0.12,10] #default for GTE = [-10,0.12,10], default original: 3
    
    if(relativeBins):                           
                                  
       for i in range(0,F_min.shape[0]-1):                          
            #print str(F_min[i]- 0.001)                         
            #print str(F_max[i]- 0.001)                         
            bins = bins + 1                         
            binEdges = np.linspace(F_min[i]- epsilon, F_max[i]+ epsilon, 4)                         
            #binEdges = np.linspace(F_min[i]-epsilon, F_max[i]+epsilon, bins+1)                         
            for j in range( 0,(len(binEdges)-2)):                           
                for k in range(len(F)):                         
                    if diff_F[k,i] >= binEdges[j] and diff_F[k,i] < binEdges[j+1]:                          
                        hits.append(1)                          
                    else:                           
                        hits.append(0)                          
            for k in range(len(diff_F)):                                    
               D[hits[k], i] = j
               #print D[hits[k], i]
               #print j
    else:                           
        #print 'Len(bins) '+str(len(bins))                           
        if(len(bins) == 1):                         
                                  
                                        
            binEdges = np.linspace(F.min()- epsilon, F.max() + epsilon, 4)                            
                                        
        else:                           
            binEdges = bins;                            
        hits = []                           
       
        #print F
        #print binEdges
        for j in range(len(binEdges)-1):                          
            for i in range(F.shape[0]):                         
                for k in range(F.shape[1]):

                    if (F[i,k] >= binEdges[j] and F[i,k] < binEdges[j+1]):
                        #if (diff_F[i,k] >= binEdges[j] and diff_F[i,k] < binEdges[j+1]):
                            D[i,k] = j
                            #print j
                                
                                                    
        if(debug):                          
            print('Global bin edges set at: ');                            
            for j in range(len(binEdges)):                            
                print "%.2f" %( binEdges[j])                            
                                        
    #print F                               
    #print D.T
    for i in range(int(D.shape[0])):
      for j in range(int(D.shape[1])):
        D[i,j] = D[i,j] + 1
    #print D.T
    return D.T    
    #return D

