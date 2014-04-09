import os, sys
target = 'C:/Python27/Connectomics - Python/results/appended_output.csv'
src1 = 'C:/Python27/Connectomics - Python/results/pearsonsCorrelation_valid_20140225-183626.csv'
src2 = 'C:/Python27/Connectomics - Python/results/pearsonsCorrelation_test_20140225-183626.csv'
tf = open(target, 'a')
tf.write(open(src1).read())
tf.write(open(src2).read())
tf.close()
