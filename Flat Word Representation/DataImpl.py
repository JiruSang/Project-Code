import numpy as np

'''
Get key word from dictionary

'''

def getKeyWordsDic(path='data/tm_keywords_phrase.txt'):

    dic = dict()

    file = open(path,'r')

    for line in file.readlines():

        key = line.split('=')[0]

        value = line.split('=')[1]

        dic[key] = (float)(value)



    return dic



'''
Vectorized the text by using one hot encoding
'''

def getOneHotVec(sentence='',dic=dict()):

    vec = []

    for (key, value) in dic.items():

        if key in sentence.split(' '):

            vec.append(1)

        else:

            vec.append(0)


    return np.array(vec)


'''
Vectorized the text by using one hot encoding  Weight coding
'''

def getRealVec(sentence='',dic=dict()):

    vec = []

    for (key, value) in dic.items():

        if key in sentence.split(' '):

            vec.append(value)

        else:

            vec.append(0)


    return vec

'''
Read all the data
'''

def  getAllData(filepath='',isOnehot=False,dic=None):


    labels = []



    file = open(filepath,'r')

    lines = file.readlines()

    data = []

    for line in lines:

        label = float(line.split('@')[0])

        sentence = line.split('@')[1]

        if(isOnehot):

            vec = getOneHotVec(sentence,dic)
        else:
            vec = getRealVec(sentence,dic)


        labels.append([label])

        data.append(vec)


    return np.array(data),np.array(labels)





if __name__ == '__main__':


    dic = getKeyWordsDic()

    for (key,value) in dic.items():

        print(key,value)

    print(len(dic))





