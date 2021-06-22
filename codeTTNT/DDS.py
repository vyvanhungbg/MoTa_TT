def DDS(maTranKe , T0 , goal, k):
    ds = k
    listV = [Vn[0] for Vn in maTranKe] # list chua cac dinh

    visited = [False for i in range(len(maTranKe))]
    QAndS = []

    QAndS.append(T0)
    visited[listV.index(T0)] = True # set vi tri tra ve tuong ung cua dinh T0 = true

    path =[]
    print(["---"],["---"], ["---"], QAndS, ["---"])
    while QAndS:
        s = QAndS.pop(0)
        path.append(s)

        if(s==goal):
            break
        dn = int(maTranKe[listV.index(path[-1])][-1])
        if  dn >=0 and dn<= ds-1:
             for icuoi in range(len(maTranKe[listV.index(s)]) - 2, -1, -1):
                 i = maTranKe[listV.index(s)][icuoi]
                 if not visited[listV.index(i)]:
                     QAndS.insert(0, i)
                     visited[listV.index(i)] = True
        elif dn ==ds:
            for i in maTranKe[listV.index(s)][:-1]:
                if not visited[listV.index(i)]:
                    QAndS.append(i)
                    visited[listV.index(i)] = True
        elif dn ==ds+1:
            ds = ds+k
            if k==1:
                for i in maTranKe[listV.index(s)][:-1]:
                    if not visited[listV.index(i)]:
                        QAndS.append(i)
                        visited[listV.index(i)] = True
            else:
                for icuoi in range(len(maTranKe[listV.index(s)]) - 2, -1, -1):
                    i = maTranKe[listV.index(s)][icuoi]
                    if not visited[listV.index(i)]:
                        QAndS.insert(0, i)
                        visited[listV.index(i)] = True


        print(path[-1], maTranKe[listV.index(path[-1])][-1] ,maTranKe[listV.index(path[-1])][1:-1], QAndS, path, end='')
        print("")
    return path

maTranKe = []
v = int(input("So dinh : "))
for i in range (0,v):
    maTranKe.append(list(map(str,input().split())))
print("Ket thuc tim thay dinh ___ path : ",DDS(maTranKe,'A','I',2))