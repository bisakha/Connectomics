function [prediction_discrete, variable_importance] = cl_random_forest(data, target, TRAIN_indx, TEST_indx)
% model = svm_train(target(TRAIN_indx),data(TRAIN_indx,:), options);
    model = TreeBagger(100,data(TRAIN_indx,:), target(TRAIN_indx), 'Method', 'classification','OOBVarImp','On');
    variable_importance = model.OOBPermutedVarDeltaError; 
   % model = NaiveBayes.fit(data(TRAIN_indx,:), target(TRAIN_indx));
   prediction_discrete = model.predict(data(TEST_indx,:));
   
   % [prediction_discrete, ~, prediction_continuous] = svm_predict(nan(length(TEST_indx),1),data(TEST_indx,:), model)
