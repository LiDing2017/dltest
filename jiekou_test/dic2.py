
def dic1():
    f = open('./data.txt')
    dic={}
    i=0
    with open('./data.txt') as f:
        for lis in f:
            dic.setdefault(i, []).append(lis[0])
            dic.setdefault(i, []).append(lis[2])
            i = i + 1
    return dic