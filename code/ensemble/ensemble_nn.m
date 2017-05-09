fluorescenceFile = 'fluorescence_network _check _ 2.txt';
networkFile = 'network_network _check _ 2.txt';
F = load_data(fluorescenceFile);
[D1, G] = discretizeFluorescenceSignal(F, 'conditioningLevel', 0.10, 'bins', [-10,0.12,10]);
AUC = [];
auc_vector = [];
for k = 1:1000
rng shuffle;
D = D1(randsample(1:179497, 500),:);
network = readNetworkScores(networkFile);
scores_Correlation =  full(corrcoef(D));
scores_CrossCorrelation =  full(computeCrossCorrelation(D));
scores_IGGini =  full(computeIGGini(D));
scores_MI =  full(computeMI(D));
scores_Granger =  full(computeGranger(D));
scores_GTE =  full(computeGTE(D, G));
 for i1 = 1:10
 
 inputs(:,1) = reshape(scores_Correlation, 10000,1);
 inputs(:,2) = reshape(scores_CrossCorrelation, 10000,1);
 inputs(:,3) = reshape(scores_IGGini, 10000,1);
 inputs(:,4) = reshape(scores_MI, 10000,1);
 inputs(:,5) = reshape(scores_Granger, 10000,1);
 inputs(:,6) = reshape(scores_GTE, 10000,1);
  % inputs = scores_ensemble _ 2_ 8;
 targets = reshape(full(network), 10000,1);


for j = 1:10
data_splits=split_data_multiclass(targets,1, 10);
col = 0;
for i = 1:length(data_splits)
    test_index = data_splits{i};
    train_index = cell2mat(data_splits(setdiff(1:10,i)));

    hiddenLayerSize = 10;
    net = fitnet(hiddenLayerSize);
    [net,tr] = train(net,data(TRAIN_indx,:)', target(TRAIN_indx)');
    outputs = net(data(TEST_indx,:)');
 close all;
col = col+1;
    
    auc_vector(j,col) = auc(cell2mat(outputs),targets(test_index));

end
end
vec = mean(auc_vector);
mean(mean(auc_vector));
std(vec);
 %%%%%%%%%%% SVM code ends here
 
 AUC(i1) = mean(mean(auc_vector));
end
