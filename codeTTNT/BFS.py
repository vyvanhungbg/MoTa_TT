


def BFS(maTranKe , T0 , goal):
    listV = [Vn[0] for Vn in maTranKe] # list chua cac dinh

    visited = [False for i in range(len(maTranKe))]
    queue = []

    queue.append(T0)
    visited[listV.index(T0)] = True # set vi tri tra ve tuong ung cua dinh T0 = true

    path =[]
    print(["---"], ["---"], queue, ["---"])
    while queue:
        s = queue.pop(0)
        path.append(s)

        if(s==goal):
            break
        for i in maTranKe[listV.index(s)]:
            if not visited[listV.index(i)]:
                queue.append(i)
                visited[listV.index(i)] = True
        print(path[-1], maTranKe[listV.index(path[-1])][1::], queue, path)

    return path







maTranKe = []
v = int(input("So dinh : "))
for i in range (0,v):
    maTranKe.append(list(map(str,input().split())))
print("Ket thuc tim thay dinh ___ path : ",BFS(maTranKe,'A','R'))
