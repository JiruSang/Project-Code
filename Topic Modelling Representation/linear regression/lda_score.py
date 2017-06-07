import os
import numpy as np
import lda
from sklearn import linear_model
from matplotlib import pyplot as plt


# read a file and return the worddict, score and question type
def readFile(filePath, fileName):
    name = fileName.strip(".txt")
    question = name.split("_")[0]
    score = float(name.split("@")[1])
    word_dict = {}
    with open(filePath + fileName) as file:
        for line in file:
            lines = line.strip().split(" ")
            for word in lines:
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    return question, score, word_dict

# merge the questions to a dict, return the matrix data and vocab
def merge_word_dict(word_dict_list):
    word_set = set()
    for dict in word_dict_list:
        for word in dict:
            word_set.add(word)
    word_index = {}
    vocab = []
    index = 0
    for word in word_set:
        word_index[word] = index
        vocab.append(word)
        index += 1
    print (index, len(word_dict_list))
    data = np.zeros((len(word_dict_list), index), dtype=int)
    dict_index = 0
    for dict in word_dict_list:
        for word in dict:
            index = word_index[word]
            data[dict_index, index] += 1
        dict_index += 1
    return data, vocab

#print the topic n words
def print_word(topic_word, vocab, n):
    file = open("topic_word.txt", "w")
    M, N = topic_word.shape
    print (M, N)
    for i in range(M):
        file.write("topic%d:" % i)
        word_weight = topic_word[i, :]
        word_index = np.argsort(word_weight)[-(n+1):-1]
        str = ""
        for index in word_index:
            word = vocab[index]
            weight = word_weight[index]
            newstr = " %s\t%.4f" % (word, weight)
            str = newstr + str
        file.write("%s\n" % str)
    file.close()

if __name__ == "__main__":
    pathDir = os.listdir("./all")
    fileName_list = []
    question_list = []
    score_list = []
    word_dict_list = []
    for fileName in pathDir:
        # can change the file. From all questions or from each question separately
        question, score, word_dict = readFile("./all/", fileName)
        question_list.append(question)
        score_list.append(score)
        word_dict_list.append(word_dict)
        fileName_list.append(fileName)
    data, vocab = merge_word_dict(word_dict_list)
    model = lda.LDA(n_topics=6, n_iter=300, random_state=1)
    model.fit(data)
    topic_word = model.topic_word_
    n = 5 # print the topic n words
    print_word(topic_word, vocab, n)
    file = open("doc_topic.txt", "w")
    doc_topic = [[] for i in range(4)]
    doc_score = [[] for i in range(4)]
    for i in range(len(question_list)):
        for j in range(4):
            if question_list[i] == "Q" + str(j + 1):
                doc_topic[j].append(list(model.doc_topic_[i]))
                doc_score[j].append(score_list[i])
    clf = linear_model.LinearRegression()
    predict_score_list = []
    for j in range(4):
        x = range(len(doc_score[j]))
        X = np.array(doc_topic[j])
        Y = np.array(doc_score[j])
        if len(Y) == 0: continue
        clf.fit(X, Y)
        score = clf.predict(X)
        predict_score_list.extend(list(score))
        #average loss or RMSE
        #rmse = (sum(abs(score - Y)) / len(Y))
        rmse = (sum((score - Y) ** 2) / len(Y)) ** 0.5
        plt.figure(j + 1)
        plt.plot(x[:100], score[:100], label="predict_score", color="yellowgreen", linewidth=2)
        plt.scatter(x[:100], Y[:100], label="origin score", color="lightskyblue", linewidths=1)
        plt.title("RMSE is %.3f" % rmse)
        plt.legend()
        plt.savefig("Q" + str(j + 1) + ".png")
    for i in range(len(model.doc_topic_)):
        doc_list = np.array(model.doc_topic_[i], dtype=str)
        doc_str = "\t".join(list(doc_list))
        file.write("doc %d--origin score:%.2f, predict score:%.2f %s\n" % (i, score_list[i], predict_score_list[i], doc_str))
    file.close()


