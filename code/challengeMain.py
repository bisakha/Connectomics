####################################################################################

#### CHALLENGE MAIN

####################################################################################

#### Example generating a challenge submission. Loads the provided fluorescence file

#### and performs the reconstruction (based on sample algorithms). As output it generates

#### a scoring matrix whose ROC is computed against the true network (if provided).

####

#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.

#### Contact: causality@chalearn.org.



# Initializations ==> see below user defined options

import sys

import time

import os

import numpy

import scipy

import csv

import pylab as pl

import matplotlib.pyplot as plt

from scipy.sparse import *

from sklearn import metrics

from datetime import date

from datetime import datetime

from numpy import *

from scipy import sparse

import scipy.io as sio

from StringIO import StringIO





from plotROC import plotROC

from reshapeScoresMatrix import reshapeScores

from reshapeNetwork import reshapeNetwork

from iter_loadtxt import iter_loadtxt

from writeNetworkScoresInCSV import writeNetworkScoresInCSV

from randomScoreCode import randomScore

from computeCrossCorrelation import computeCrossCorrelation

from readNetworkScoresCode import readNetworkScores

from computePearsonsCorrelation import computePearsonsCorrelation

from computeIGCI import computeIGCI

from computeMI import computeMI

if (os.name == "nt"):

       os.system('cls')

       filesep = '\\'

else:

       filesep = filesep

              

tic = time.clock();



funcdict = {

  'randomScore': randomScore,

  'crossCorrelation':computeCrossCorrelation,

  'pearsonsCorrelation':computePearsonsCorrelation,

  'information-geometry-causal-inference':computeIGCI,

  'mutualinformation': computeMI

}



def main():

           

# Begin -- User defined options --

       default_path_1 = os.getcwd()

       os.chdir(default_path_1)

       default_path = os.path.normpath(os.path.join(os.getcwd(), ".."))

       challengeFolder = default_path + filesep

	# challengeFolder = default_path + '\\'

       dataDirectory = challengeFolder +'data'

       submissionDirectory = challengeFolder + 'results' # Where ready-to-submit result files are found

       modelDirectory = challengeFolder + 'models'       # Where trained predictive models end up


       
       file_count = 1

       networkIdNames = []



       #networkIdNames.append('normal-1')        # IMPORTANT: these are the base names of your data 

       #networkIdNames.append('normal-2')

       #networkIdNames.append('iNet1_Size100_CC01inh')

       #networkIdNames.append('iNet1_Size100_CC02inh')

       #networkIdNames.append('iNet1_Size100_CC03inh')

       #networkIdNames.append('iNet1_Size100_CC04inh')

       #networkIdNames.append('iNet1_Size100_CC05inh')

       #networkIdNames.append('iNet1_Size100_CC06inh')

       networkIdNames.append('mockvalid')  # You can run the code as is with these options

       networkIdNames.append('mocktest')   # To generate a challenge submission, substitute mockvalid and mocktest for valid and test

                                           # that are the challenge datasets.
 
       scoringMethods = [];

       scoringMethods.append('pearsonsCorrelation'); # We provide 3 "basic" examples of scoring methods. You need to write your own.

                                                     # We did not implement GTE (see the Matlab and C++ code for that).

       #scoringMethods.append('crossCorrelation');  

       #scoringMethods.append('randomScore');

       #scoringMethods.append('computeGranger');

       #scoringMethods.append('information-geometry-causal-inference');

       #scoringMethods.append('mutualinformation'); 
                                                

       modelName = 'sample_model' # Name of the model used by the trainedPredictor scoring method

       concatenateScores = 0;     # 1 if all scores from various networks are appended to the same file (for each method)

       # End -- User defined options --

       # Initializations

       

       if not os.path.exists(submissionDirectory):

           os.makedirs(submissionDirectory)



       the_date = datetime.now()

       timestr = time.strftime("%Y%m%d-%H%M%S")

       extension='.txt';

       # logfile = submissionDirectory + '\\' + 'logfile.txt'

       logfile = submissionDirectory + filesep + 'logfile.txt'

       flog=open(logfile, 'a');

       print('==========================================================\n')

       print('\n ChaLearn connectomics challenge, sample code version '+sys.version+'\n')

       print(' Date and time started: ' + the_date.strftime("%d/%m/%Y %H:%M:%S")+'\n')

       print(' Saving AUC results in ' + logfile+'\n')

       print('==========================================================\n\n')


       start = time.time()




       metNum=len(scoringMethods);

       netNum=len(networkIdNames);

       scores = numpy.empty((netNum,metNum))



       for j in range(0,metNum):    

          scoringMethod = scoringMethods[j];      

          # scoreFile = submissionDirectory + '\\' + scoringMethod + '_' +"_".join(str(x) for x in networkIdNames )+timestr+'.csv';

          target = submissionDirectory + filesep + scoringMethod + '_' +"_".join(str(x) for x in networkIdNames )+timestr+'_kaggle_ready.csv'; 
       
          tf = open(target, 'a')

          scoreFile = submissionDirectory + filesep + scoringMethod + '_' +"_".join(str(x) for x in networkIdNames )+timestr+'.csv'; 

# Loop over all networks you want to process   

          for i in range(0,netNum):



              networkId = networkIdNames[i];

              print('***'+ scoringMethod  +' on '+networkId+' ***\n\n' );



# Load the Fluorescence signal

              # fluorescenceFile = dataDirectory + '\\'+ 'fluorescence_'+networkId+extension;

	      fluorescenceFile = dataDirectory + filesep+ 'fluorescence_'+networkId+extension;

              

              #F = loadtxt(fluorescenceFile,delimiter=",")
	      F = iter_loadtxt(fluorescenceFile)

# Compute the scores for all pairs of neurons i, j

              tic = time.clock()

              print('Computing scores with ' + scoringMethod + '\n')

              if scoringMethod == 'trainedPredictor':

                  # arg =  modelDirectory + '\\' + modelName + '.mat'

		  arg =  modelDirectory + filesep + modelName + '.mat'

              else:

                  arg = 'false'

        

              scores = funcdict[scoringMethod](F, arg)

              #scores =    numpy.corrcoef(F, rowvar = 0)

              

# Note: these scoring methods do not make use of available neuron

# positions (in their 2-D layout simulating neuron cultures).

              toc = time.clock()



#Write the scores to the submission directory, ready to be submitted

              # resuFile = submissionDirectory + '\\'+scoringMethod+'_'+networkId+'_'+timestr+'.csv';

 	      resuFile = submissionDirectory + filesep+scoringMethod+'_'+networkId+'_'+timestr+'.csv';

              if ~concatenateScores:

                  scoreFile = resuFile

              print 'Writing ' + scoreFile + ' \n'

              if scoringMethod == 'randomScore':

                         scores_dense =  scores.toarray()

              else:

                         scores_dense = scores



              writeNetworkScoresInCSV(scoreFile, scores_dense, networkId)

              if file_count == 1:
                     
                 tf.write(open(scoreFile).read())

                 file_count = file_count + 1

              else:
                     
                 src1 = open(scoreFile)

                 src1.readline()

                 tf.write(src1.read())

                 src1.close()

# If we have the network architecture... compute/plot the ROC curve:

# (network architecture provided only for training data to the participants)

              # networkFile = dataDirectory +'\\'+'network_' +networkId +extension;
	      networkFile = dataDirectory + filesep + 'network_' + networkId + extension        

              

              if os.path.exists(networkFile):

                  print'Computing ROC with using network ' + networkFile + '\n'

                  network = readNetworkScores(networkFile);          

                  

                  if scoringMethod == 'randomScore':

                         scores_dense =  scores.toarray()

                  else:

                         scores_dense =  scores    

                  pred = reshapeScores(scores_dense)

                  true = reshapeNetwork(network)

                  

                  ###############################################



                  fpr, tpr, thresholds = metrics.roc_curve(true,pred)

                  

                  print('\n==> AUC = '+ str(metrics.auc(fpr,tpr))+'\n');

                  

                  

                  resuFile = scoringMethod+'_'+networkId+'_'+timestr+'.png'

                  

                  fullpath = os.path.join(submissionDirectory , resuFile)

                  plotROC(fpr,tpr,fullpath)



                  flog.write(the_date.strftime("%d/%m/%Y %H:%M:%S")+'\t'+scoringMethod+'\t'+networkId+'\t'+'%.4f\n' % ((metrics.auc(fpr, tpr))))
 


#close all open files
       end = time.time()

       #print networkId
                  
       print end - start

       print the_date.strftime("%d/%m/%Y %H:%M:%S")+' Challenge solved.' +'\n'

       toc = time.clock();

       flog.close()
       
       tf.close()


if __name__=="__main__":

    main()

