#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.


def reshapeScores(scores_dense):
    y_pred = []
    y_pred_1 = []
    for i in range(scores_dense.shape[0]):
        for j in range(scores_dense.shape[1]):
            y_pred_1.append(scores_dense[i][j])
            if scores_dense[i][j] > 0:
               scores_dense[i][j] = int(1)
               y_pred.append(int(1))
            else:
               scores_dense[i][j] = int(0)
               y_pred.append(int(2))
        

    return y_pred_1
