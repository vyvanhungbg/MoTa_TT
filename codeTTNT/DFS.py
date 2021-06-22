


def DFS(maTranKe , T0 , goal):
    listV = [Vn[0] for Vn in maTranKe] # list chua cac dinh

    visited = [False for i in range(len(maTranKe))]
    stack = []

    stack.append(T0)
    visited[listV.index(T0)] = True # set vi tri tra ve tuong ung cua dinh T0 = true

    path =[]

    print(["---"], ["---"], stack,["---"])
    while stack:
        s = stack.pop(0)
        path.append(s)

        if(s==goal):
            break

        for icuoi in range(len(maTranKe[listV.index(s)])-1,-1,-1) :
            i = maTranKe[listV.index(s)][icuoi]
            if not visited[listV.index(i)]:
                stack.insert(0,i)
                visited[listV.index(i)] = True
        print(path[-1], maTranKe[listV.index(path[-1])][1::], stack, path)

    return path







maTranKe = []
v = int(input("So dinh : "))
for i in range (0,v):
    maTranKe.append(list(map(str,input().split())))
print("Ket thuc tim thay dinh ___ path : ",DFS(maTranKe,'A','R'))
