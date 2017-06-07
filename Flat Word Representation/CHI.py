
# build vocabulary library from all Q1 Q2 Q3 Q4 answers
def buildVocab():

    files = ["data/all_Q1_phrase.txt","data/all_Q2_phrase.txt","data/all_Q3_phrase.txt","data/all_Q4_phrase.txt"]
    vocab = []
    for file in files:

        openfile = open(file,'r')

        lines = openfile.readlines()

        for line in lines:

            items = line.split("@")[1].split(" ")
            for item in items:

                if item not in vocab:

                    vocab.append(item)



    return vocab

# read from dictionary

def getChiKeyWordsFromFile(filename="data/all_Q1_phrase.dic",rate=0.5):

    file = open(filename,'r')

    dic = dict()

    lines = file.readlines()

    lines = lines[0:int(float(len(lines))*(float)(rate))]

    for line in lines:

        key = line.split("=")[0]
        value = line.split("=")[1]

        dic[key] = float(value)


    return dic











def mainCHI(filename="data/all_Q1.txt",others=["data/all_Q2.txt","data/all_Q3.txt","data/all_Q4.txt"],rate=0.5):

    allItem = ["Q1","Q2","Q3","Q4"]

    others = []

    for item in allItem:

        if item not in filename:

            others.append("data/all_"+item+".txt")





    fileDic = open(filename.split(".")[0]+".dic",'w')
    vocab = buildVocab()

    # vocab = vocab[0:50]

    print("Vocab Size:"+str(len(vocab)))

    file = open(filename, 'r')
    lines = file.readlines()

    file1 = open(others[0], 'r')
    lines1 = file1.readlines()

    file2 = open(others[1], 'r')
    lines2 = file2.readlines()

    file3 = open(others[2], 'r')
    lines3 = file3.readlines()




    dic = dict()

    count = 0

    for word in vocab:

        ##计算ABCD值
        count+=1

        if(count%500==0):

            print("finished "+str(count))



        A = getCountByWordAndClass(word,lines)
        B = 0
        D = 0

        B += getCountByWordAndClass(word, lines1)+getCountByWordAndClass(word, lines2)+getCountByWordAndClass(word, lines3)
        D += getCountNoByWordAndClass(word, lines1)+getCountNoByWordAndClass(word, lines2)+getCountNoByWordAndClass(word, lines3)



        C = getCountNoByWordAndClass(word,lines)


        # print(A,B,C,D)

        chi = getCHi(A,B,C,D)

        b = '%.9e' % chi

        dic[word] = float(b)

    dicSorted = sort_by_value(dic)

    print(dicSorted)

    print(dic)

    print(type(dicSorted))

    for k,v in dicSorted:
        print(k)

        fileDic.write(str(k)+"="+str(v)+"\n")

    fileDic.close()

    print(dic)
    return dic


def sort_by_value(dic):
    dict = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    return dict



#计算卡方值
def getCHi(A,B,C,D):

    N = A+B+C+D

    item_up = A*D-B*C

    item_down = (A+C)*(A+B)*(B+D)*(C+D)+10**(-10)

    chi = float(N*item_up)/float(item_down)

    return chi


#统计在该文档出现的概率

def getCountByWordAndClass(key,lines):



    count = 0

    for line in lines:

        if key in line:

            count+=1


    return count

##统计在该文档中未出现的次数

def getCountNoByWordAndClass(key,lines):



    count = 0

    for line in lines:

        if key not in line:

            count+=1


    return count



if __name__ == '__main__':

    filename = ""

    mainCHI(filename="data/all_Q1_phrase.txt")
    mainCHI(filename="data/all_Q2_phrase.txt")
    mainCHI(filename="data/all_Q3_phrase.txt")
    mainCHI(filename="data/all_Q4_phrase.txt")


