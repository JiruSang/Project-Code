

def getSingleTypeData(filepath='all_Q1.txt'):
    openfile = open(filepath,'r',encoding='utf-8')

    sequence = ""

    while 1:

        try:
            line = openfile.readline()
        except:
            continue

        if not line:
            break
        else:

            items = line.split('@')

            sequence+=items[1]


    return sequence


if __name__ == '__main__':

    print("")





