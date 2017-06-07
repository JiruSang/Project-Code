from CHI import getChiKeyWordsFromFile
from tfidf import getTfidfDic

import numpy as np

#vectorize the document
def vertorizeData(filename="data/all.txt",isTopicModel=True,isCHi=True,isTFIDF=True,rate=0.5,isOneHot=False):

    file = open(filename,'r')

    lines = file.readlines()

    dicTopic = getTopicKeyWords(rate=rate)


    chiDicPath = filename.split(".")[0]+"."+"dic"
    dicChi = getChiKeyWordsFromFile(filename=chiDicPath,rate=rate)

    dicTFIDFList = getTfidfDic()

    dicTFIDFList = dicTFIDFList[0:int(float(len(dicTFIDFList)) * (float)(rate))]

    dicTFIDF = dict()

    data = []

    labels = []

    for k,v in dicTFIDFList:

        dicTFIDF[k] = float(v)


    for line in lines:

        label = line.split("@")[0]

        context = line.split("@")[1]

        dataTemp = []

        labels.append([float(label)])


        #loading topic modeling
        if(isTopicModel):

            if(isOneHot):
                for k in dicTopic:
                    if k in context:
                        dataTemp.append(1)

                    else:
                        dataTemp.append(0)

            else:
                for k in dicTopic:
                    if k in context:
                        dataTemp.append(dicTopic[k])

                    else:
                        dataTemp.append(0)

        #lodaing chi-square
        if (isCHi):

            if (isOneHot):
                for k in dicChi:
                    if k in context:
                        dataTemp.append(1)

                    else:
                        dataTemp.append(0)

            else:
                for k in dicChi:
                    if k in context:
                        dataTemp.append(dicChi[k])

                    else:
                        dataTemp.append(0)


         # loading TF-IDF
        if (isTFIDF):

            if (isOneHot):
                for k in dicTFIDF:
                    if k in context:
                        dataTemp.append(1)

                    else:
                        dataTemp.append(0)

            else:
                for k in dicTFIDF:
                    if k in context:
                        dataTemp.append(dicTFIDF[k])

                    else:
                        dataTemp.append(0)


        data.append(dataTemp)


    return np.array(data),np.array(labels)




def vectorizeSingleItem(filename="data/all.txt",line="",isTopicModel=True,isCHi=True,isTFIDF=True,rate=0.5,isOneHot=False):

    lines = [line]

    dicTopic = getTopicKeyWords(rate=rate)

    chiDicPath = filename.split(".")[0] + "." + "dic"
    dicChi = getChiKeyWordsFromFile(filename=chiDicPath, rate=rate)

    dicTFIDFList = getTfidfDic()

    dicTFIDFList = dicTFIDFList[0:int(float(len(dicTFIDFList)) * (float)(rate))]

    dicTFIDF = dict()

    data = []

    labels = []

    for k, v in dicTFIDF:
        dicTFIDF[k] = float(v)

    for line in lines:

        label = 0

        context = line

        dataTemp = []

        labels.append([float(label)])

        # loading topic modeling
        if (isTopicModel):

            if (isOneHot):
                for k in dicTopic:
                    if k in context:
                        dataTemp.append(1)

                    else:
                        dataTemp.append(0)

            else:
                for k in dicTopic:
                    if k in context:
                        dataTemp.append(dicTopic[k])

                    else:
                        dataTemp.append(0)

        # loading chi-square
        if (isCHi):

            if (isOneHot):
                for k in dicChi:
                    if k in context:
                        dataTemp.append(1)

                    else:
                        dataTemp.append(0)

            else:
                for k in dicChi:
                    if k in context:
                        dataTemp.append(dicChi[k])

                    else:
                        dataTemp.append(0)

            # loading tf-idf
            if (isTFIDF):

                if (isOneHot):
                    for k in dicTFIDF:
                        if k in context:
                            dataTemp.append(1)

                        else:
                            dataTemp.append(0)

                else:
                    for k in dicTFIDF:
                        if k in context:
                            dataTemp.append(dicTFIDF[k])

                        else:
                            dataTemp.append(0)

        data.append(dataTemp)
        labels.append(label)

    return np.array(data), np.array(labels)








def getTopicKeyWords(filename="data/tm_keywords.txt",rate=0.5):

    file = open(filename,'r')

    lines = file.readlines()

    dic = dict()

    for line in lines:
        if("=" in line):
            key = line.split("=")[0]
            value = line.split("=")[1]

            dic[key] = float(value)



    return dic





