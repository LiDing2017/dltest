fp=open('./data.txt')
print type(fp)
dic = {}
i = 1
for lis in fp:

    dic.setdefault(i,[]).append(lis[0])
    dic.setdefault(i,[]).append(lis[2])
    i=i+ 1
print dic