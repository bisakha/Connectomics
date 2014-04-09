#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.

from sklearn import metrics
import pylab as pl


def plotROC(fpr,tpr,fullpath):
        pl.clf()
        pl.plot(fpr, tpr, label='ROC curve (area = %0.4f)' % metrics.auc(fpr,tpr))
        pl.plot([0, 1], [0, 1], '--')
        pl.xlim([0.0, 1.0])
        pl.ylim([0.0, 1.0])
        pl.xlabel('False Positive Rate')
        pl.ylabel('True Positive Rate')
        pl.title('Receiver operating characteristic ')
        pl.legend(loc="lower right")
        pl.savefig(fullpath)
        #pl.show()
        pl.close()
        

