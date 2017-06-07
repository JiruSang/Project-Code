from sklearn import linear_model
import matplotlib.pyplot as plt

from DataImpl import getKeyWordsDic,getRealVec,getOneHotVec

from Vectorize import vertorizeData,vectorizeSingleItem

from sklearn.externals import joblib

from sklearn import preprocessing




from sklearn.decomposition import PCA

import numpy as np


# flat terms vector representation
class ReGression():
    def __init__(self,filepath):

        self.filepath = filepath


    def trainRegression(self):

# Set true or false to add feature selection method
        isTopicModel = True

        isCHIModel = True

        isTFIDF = True

        rate = 0.01

        isOneHot = True

        filename = self.filepath


        tips = ""

        if isTopicModel:
            tips+="Topic Model "

        if isCHIModel:
            tips += "CHI Model "

        if isTFIDF:
            tips += "TFIDF Model "

        if isOneHot:

            tips += " OneHot Encode"

        else:
            tips+=" Value Encode"

        print('start loading key words from ', tips)


        print('Vecterized the data, we can get the data and labels')
        x_values, y_values = vertorizeData(filename=filename,isTopicModel=isTopicModel,
                                           isCHi=isCHIModel,isTFIDF=isTFIDF,rate=rate,isOneHot=isOneHot)


        a = len(x_values)
        x_values = x_values[0:a]
        y_values = y_values[0:a]

        x_values = preprocessing.scale(x_values)

        pca = PCA(n_components=1, copy=True, whiten=False)

        x_1 = pca.fit_transform(x_values,y_values)

        x_train = x_values[0:int(float(len(x_values))*0.99)]
        y_train = y_values[0:int(float(len(x_values))*0.99)]

        body_reg = linear_model.LinearRegression()

        body_reg.fit(x_train, y_train)

        joblib.dump(body_reg, self.filepath + "_model.m")

        x_1_test = x_1[int(float(len(x_values))*0.97):len(x_values)]
        x_values_test = x_values[int(float(len(x_values))*0.97):len(x_values)]
        y_values_test = y_values[int(float(len(x_values))*0.97):len(x_values)]

        x_values_test, x_1_test, y_values_test = getSortedXY(x_values_test, y_values_test, x_1_test)

        print("We have training set:")
        print("num:" + str(len(x_train)) + ",dim of the X:" + str(x_train.shape))

        print("We have testing set:")
        print("num:" + str(len(x_values_test)) + ",dim of the X:" + str(x_values_test.shape))

        print('-------------------')


        y_preds = body_reg.predict(x_values_test)

        y_preds = filterY(y_preds)

        print(y_values_test)

        print("Prediction of the test data last " + str(len(x_values_test)) + " samples ")
        print(y_preds)

        loss = getLoss(y_values_test, y_preds)
        print("This Average Loss:" + str(loss))
        print()


        title = "Regression on "+self.filepath.split(".")[0]+" ("+tips+")"
        plt.suptitle(title)
        plt.scatter(x_1_test, y_values_test)
        plt.plot(x_1_test, y_preds)
        plt.show()






    def predict(self,sentence):

        isTopicModel = True

        isCHIModel = False

        isTFIDF = True

        rate = 0.1

        isOneHot = False

        filename = self.filepath

        tips = ""

        if isTopicModel is True:
            tips += "Topic Model "

        else:
            tips+=""

        if isCHIModel is True:
            tips += "CHI Model "
        else:
            tips += ""


        if isTFIDF is True:
            tips += "TFIDF Model "
        else:
            tips+=""

        if isOneHot is True:

            tips += " OneHot Encode"



        else:
            tips += " Value Encode"

        print('start loading key words from ', tips)

        print('Vecterized the data, we can get the data and labels')
        x_values, y_values = vertorizeData(filename=filename, isTopicModel=isTopicModel,
                                           isCHi=isCHIModel, isTFIDF=isTFIDF, rate=rate, isOneHot=isOneHot)

        x_pred,lab = vectorizeSingleItem(filename=filename,line=sentence, isTopicModel=isTopicModel,
                                     isCHi=isCHIModel, isTFIDF=isTFIDF, rate=rate, isOneHot=isOneHot
                                     )


        print(x_values)

        print(y_values)

        print(len(x_values), len(y_values))

        body_reg = linear_model.LinearRegression()

        body_reg.fit(x_values, y_values)

        y_pred = body_reg.predict(x_pred)

        return y_pred


def getSortedXY(X_values,Y_values,x_1):

    dic = {}

    for i in range(len(x_1)):

        dic[x_1[i][0]] = Y_values[i][0]

    dic = sort_by_key(dic)

    X_values_new = X_values
    print(dic)
    count = 0
    for k,v in dic:
        index = getIndexByValue(x_1,k)
        x_1[count] = [k]
        Y_values[count] = [v]
        X_values_new[count] = X_values[index]

        count+=1

    # print(x_1)
    return X_values_new,x_1,Y_values

def getIndexByValue(x_1,value):

    count = -1

    for i in x_1:
        if i[0]==value:

            break
        count+=1

    return count


def filterY(y_pred):

    for i in range(len(y_pred)):

        if (abs(y_pred[i][0]) > 4):
            y_pred[i][0] = 3

    return y_pred




# calculate the average loss of the prediction
def getLoss(y_values,y_pred):
    loss = 0.0
    for i in range(len(y_values)):
        if(abs(y_pred[i][0])<5):
            loss = loss + abs(y_values[i][0] - y_pred[i][0])

    loss=(loss/float(len(y_values)))

    return loss



def sort_by_key(dic):
    dict = sorted(dic.items(), key=lambda d: d[0], reverse=False)
    return dict


if __name__ == '__main__':
    # can read the answers from all answers or read the answers from Q1 2 3 4separately
    rg = ReGression(filepath="data/all.txt")
    rg.trainRegression()

