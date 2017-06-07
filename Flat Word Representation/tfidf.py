# -*- coding: utf-8 -*-\
import string
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from FileUtils import getSingleTypeData


# TF-IDF method to do feature selection
def getTfidfDic(rate=0.5):
    corpus = []
    tfidfdict = {}
    f_res = open('sk_tfidf.txt', 'w', encoding='utf-8')

    label_dic = ["Q1","Q2","Q3","Q4"]

    print(label_dic)

    for lab in label_dic:

        # can be used to select unitary terms or binary terms from separate files
        #filepath = "data/all_" + lab + "_phrase.txt"
        filepath="data/all_"+lab+".txt"

        corpus.append(getSingleTypeData(filepath))


    vectorizer = CountVectorizer() # This class converts the words in the text into word frequency matrices, the matrix element,a [i][j], denotes the word frequency of word j in class i
    transformer = TfidfTransformer()  # This class counts the tf-idf weights for each term
    tfidf = transformer.fit_transform(
        vectorizer.fit_transform(corpus))  #The first fit_transform calculate tf-idf, the second fit_transform transforms the text into the word frequency matrix

    word = vectorizer.get_feature_names()  # Get all teh terms from bag of words

    print(len(word))
    weight = tfidf.toarray()  # extract TF-IDF, element a[i][j] denotes teh weight of term j in document i
    for i in range(len(weight)):  # print TF-IDF weight for each document. The first for loop travers all the documents，the second for loop travers all the terms in this docrment
        for j in range(len(word)):
            getword = word[j]
            getvalue = weight[i][j]
            if getvalue != 0:  # remove the element which value is zero
                if getword in tfidfdict:  # updat the overall value of TF-IDF
                    tfidfdict[getword] += (float)(getvalue)
                else:
                    tfidfdict.update({getword: getvalue})

    tfidfdict = sorted(tfidfdict.items(), key=lambda d: d[1],reverse=True)







    return tfidfdict


def sort_by_value(dic):
    dict = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    return dict


if __name__ == "__main__":
    tfidfdict = getTfidfDic()
    print(tfidfdict)

