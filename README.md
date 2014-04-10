Connectomics
============
=============================================================================

*** First Connectomics Challenge Starter Kit
*** http://connectomics.chalearn.org/
*** Version 1 - February 2014

=============================================================================

ALL INFORMATION, SOFTWARE, DOCUMENTATION, AND DATA ARE PROVIDED "AS-IS". CHALEARN, KAGGLE AND/OR OTHER ORGANIZERS DISCLAIM ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY PARTICULAR PURPOSE, AND THE WARRANTY OF NON-INFRIGEMENT OF ANY THIRD PARTY'S INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT SHALL THE ORGANIZERS BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF SOFTWARE, DOCUMENTS, MATERIALS, PUBLICATIONS, OR INFORMATION MADE AVAILABLE FOR THE CHALLENGE. 

=============================================================================

The goal of the challenge is to predict whether there is a (directed) connection between neuron i and neuron j in a network of 1000 neurons (self-connections permitted). We provide one hour of recording of the activity of all neurons as time series and the position of the neurons (arranged on a flat surface). The data, which are simulated, reproduce as faithfully as possible neural activity measured with calcium fluorescence imaging of neural cultures.

SAMPLE DATA
===========
The starter kit includes sample data files from 100 and 1000 neuron networks, that are used for validation and testing in the challenge.

1) FLUORESCENCE = fluorescence_mockvalid.csv and fluorescence_mocktest.csv: comma separated files including time series of neural activity, each row representing a sample and each column a neuron. Signal is sampled at 20ms intervals.

2) NETWORK POSITIONS = networkPositions_mockvalid.csv and networkPositions_mocktest.csv: comma separated files, each row representing a neuron. First column is the X position and second column the Y position. Neurons span a 1mm2 square area.

3) NETWORK = network_mockvalid.csv and network_mocktest.csv: comma separated files representing the network architecture. Each row is a connection. The column structure is of the form I,J,W denoting a connection from I to J with weight W. Connections with positive weight (usually 1) are present. Pairs that are absent or have a weight -1 are inexistent or blocked in the simulations (which is the same thing as far as this challenge is concerned).

All data have the same three files, prefixed with fluorescence_, networkPositions_, and network_. The postfix "mockvalid"  or "mocktest" is the network name. When you substitute the sample data for the challenge data, this should be replaced.

SAMPLE NETWORK RECONSTRUCTION CODE
==================================
The main entry point of the starter kit is:
> $ python challengeMain.py

The script takes a few minutes to run on the sample network of 100 neurons and the actual validation and test networks of 1000 neurons. 

1) Load the fluorescence file as a matrix F, neurons in columns; each line is a time sample.

2) Perform various steps to compute scores for neuron i -> neuron j using a choice of methods, including the GTE algorithm, from Stetter, O., Battaglia, D., Soriano, J. & Geisel, T. Model-free reconstruction of excitatory neuronal connectivity from calcium imaging signals. PLoS Comput Biol 8, e1002653 (2012). This code also produces graphs similar to those of the paper.

The resulting "scores" matrix is a matrix N x N, N being the number of neurons, each entry (i, j) indicating the "confidence" that neuron i -> neuron j. Presently, only random scores technique is implemented in Python.

3) Writes the scores in Kaggle submission format as a 2-column csv file
NET_neuronI_neuronJ Strength indicating the "confidence" that neuron i -> neuron j.

4) The code appends results for valid and test in Kaggle submission format in a file named as [algoname]_[dataset1]_[dataset2]_[datetime]_kaggle_ready.csv which can be submitted for evaluation.


RESULTS
================================

| Algorithm                       | Network    | Time to process big network    | OS        | Python version                     | AUC     |
|---------------------------------|------------|--------------------------------|-----------|------------------------------------|---------|
| Correlation                     | Normal-1   | 73.3740000725 s                | Windows 7 | 2.7.3  [MSC v.1500 64 bit (AMD64)] | 0.68186 |
| Correlation                     | Normal-2   | 150.825000048 s                | Windows 7 | 2.7.3  [MSC v.1500 64 bit (AMD64)] | 0.69956 |
| Correlation                     | Valid-Test | 130.039999962 s                | Windows 7 | 2.7.3  [MSC v.1500 64 bit (AMD64)] | 0.6639  |
| Correlation with discretization | Normal-1   | 565.462999821 s                | Windows 7 | 2.7.3  [MSC v.1500 64 bit (AMD64)] | 0.6752  |
|                                 |            | = 9.4244 mins                  |           |                                    |         |
| Correlation with discretization | Normal-2   | 1089.74799991 s = 18.162  mins | Windows 7 | 2.7.3  [MSC v.1500 64 bit (AMD64)] | 0.75773 |
| Correlation with discretization | Valid-Test | 1054.31400013 s = 17.572 mins  | Windows 7 | 2.7.3  [MSC v.1500 64 bit (AMD64)] | 0.87322 |



FUNCTIONS
=================================
randomScore

pearsonsCorrelation 

Crosscorrelation

Discretization

INSTALLATION
============
The code requires Python version 2.7.3

It was tested under

Intel(R) Core(TM) i7-3770 CPU @ 3.40 GHz 3.40 GHz, 16.0 GB RM, 16339 MB Swap, OS Windows 64 bit

and

Intel Core i5 CPU @ 2.53 HHz 4 GB RM, Mac OSX 10.6.8

using the following library versions:

numpy 1.7.1 
scipy 0.12.0 
pandas 0.13.0 
matplotlib 1.3.1 




=============================================================================

Acknowledgements:
This starter kit in Python was prepared by Bisakha Ray with original code authored by Javier Orlandi and Olav Stetter and MATLAB code by Isabelle Guyon and Mehreen Saeed. 

=============================================================================
