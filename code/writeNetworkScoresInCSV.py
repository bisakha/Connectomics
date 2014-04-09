#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.


import csv


def writeNetworkScoresInCSV(filename,scores,networkID):
#%writeNetworkScoresInCSV(filename,scores,networkID,separator,header)
#% will write the scores in kaggle format as a CSV file when given the network ID.  
#% scores should be an nxn matrix, whose (i,j)th entry indicates the strength of 
#% connection from neuron i to neuron j
    header = 'NET_neuronI_neuronJ'
    with open(filename, 'ab') as f:
        writer = csv.writer(f,delimiter = ',',dialect = "excel")
        writer.writerows([[header,'Strength']])
        
        
        #for i in range(0,scores.shape[0]-1):
          #for j in range(0, scores.shape[1]- 1):
        #for i in range(scores.shape[0]):
        #  for j in range(scores.shape[1]):
        for i in range(len(scores)):
         for j in range(len(scores[0])):
           v = scores[i][j]
        
           neuron_i_neuron_j_strength = networkID+'_'+str(i+1)+'_'+str(j+1)
          
           
           writer.writerows([[neuron_i_neuron_j_strength, str(v)]])
    f.close()       

