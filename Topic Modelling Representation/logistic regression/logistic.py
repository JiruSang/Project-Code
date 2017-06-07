from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
addr_q1=r"C:\Users\sony\Desktop\4-Logistic Regression\lda\q1_sample.json"
import json
def read_json(addr):
    res={}
    with open(addr)as json_file:
        res=json.loads(json_file.read())
    return res

sample_data_q1=read_json(addr_q1)

# logistic regression classifier
def logisticRregressionClassfier(data, label, myPenalty='l2', mySolver='lbfgs', inversedRegularStrength=0.5,
                                ifIntercept=True):

   lrcResult={}
   lrc = LogisticRegression(penalty=myPenalty, solver=mySolver, multi_class='multinomial', \
                            C=inversedRegularStrength, fit_intercept=ifIntercept);

   accracyScore=cross_val_score(lrc, data, label,cv=10);
   lrcResult["q1_accuracy"] = accracyScore
   lrcResult["q1_parameters"] = {"penalty": myPenalty, "solver": mySolver, \
                                                "C": inversedRegularStrength, "ifIntercept": ifIntercept}
   print(lrcResult)
   return lrcResult
logisticRregressionClassfier(sample_data_q1["doc_topic"],sample_data_q1["doc_score"])