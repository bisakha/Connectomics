fluorescenceFile = 'fluorescence_network _check _ 2.txt';
networkFile = 'network_network _check _ 2.txt';
F = load_data(fluorescenceFile);
[D1, G] = discretizeFluorescenceSignal(F, 'conditioningLevel', 0.10, 'bins', [-10,0.12,10]);
AUC = [];
auc_vector = [];
for i1 = 1:1
rng shuffle;
D = D1(randsample(1:179497, 500),:);
network = readNetworkScores(networkFile);
scores_Correlation =  full(corrcoef(D));
scores_CrossCorrelation =  full(computeCrossCorrelation(D));
scores_IGGini =  full(computeIGGini(D));
scores_MI =  full(computeMI(D));
scores_Granger =  full(computeGranger(D));
scores_GTE =  full(computeGTE(D, G));
 inputs(:,1) = reshape(scores_Correlation, 10000,1);
 inputs(:,2) = reshape(scores_CrossCorrelation, 10000,1);
 inputs(:,3) = reshape(scores_IGGini, 10000,1);
 inputs(:,4) = reshape(scores_MI, 10000,1);
 inputs(:,5) = reshape(scores_Granger, 10000,1);
 inputs(:,6) = reshape(scores_GTE, 10000,1);
 inputs = knnimpute(inputs);
 targets = reshape(full(network), 10000,1);
 scaled_data = (inputs - min(inputs(:))) ./ (max(inputs(:)-min(inputs(:)))); 
 %%%%%% SVM Code starts here %%%%%%%%%%%%%%%%%%%%
 
for j = 1:10
data_splits=split_data _multiclass(targets,1, 10);
col = 0;
for i = 1:length(data_splits)
    test_index = data_splits{i};
    train_index = cell2mat(data_splits(setdiff(1:10,i)));
  prediction_discrete = cl_random_forest(scaled_data,targets,train_index,test_index);
 %[prediction_continuous, prediction_discrete, model]=cl_SVM_mod(data, targets, train_index, test_index,'poly',1000,3);
    %[prediction_continuous, prediction_discrete, model]=cl_SVM_mod(scaled_data,targets,train_index,test_index,'linear',10);
    %[prediction_continuous, prediction_discrete, model]=cl_SVM_mod(scaled_data,targets,train_index,test_index,'rbf',1,0.1);
    col = col+1;
    
    auc_vector(j,col) = auc(cell2mat(prediction_discrete),targets(test_index));
 j
 i
    
end
end
vec = mean(auc_vector);
mean(mean(auc_vector));
std(vec);
 %%%%%%%%%%% SVM code ends here
 
 AUC(i1) = mean(mean(auc_vector));
end
