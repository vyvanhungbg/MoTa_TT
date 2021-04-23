import numpy as np
def NhapMaTran(soTienTrinh): #  n là số tiến trình  s
    List = []
    for i in range(0,soTienTrinh):
        List.append(list(map(int,input().split())))
    return np.array(List)

def NhapDuLieu(): # nhap m so trên 1 dòng
    soTienTrinh = int(input('Nhap so tien trinh : '))
    print('Nhap Allocation : ')
    All = NhapMaTran(soTienTrinh)
    print('Nhap Max : ')
    Max = NhapMaTran(soTienTrinh)
    print('Nhap Available 1 dong : ')
    Avai = NhapMaTran(1)[0] # [0] là chuyển về ma tran 1x1
    Need = Max - All
    Finish = [False for i in range(0,soTienTrinh)]
    return All , Max , Avai, Need , Finish ,soTienTrinh

def XetHeAnToan(All, Need , Work , Finish ,soTienTrinh):
    while  True:
        i = 0
        while i < soTienTrinh:
            WorkLucDau = np.copy(Work)
            if all(Need[i] <= Work) == True and Finish[i] == False:
                Work += All[i]
                Finish[i] = True
            i+=1
        if all(Finish) or (Work == WorkLucDau).all(): # neu ma tat ca Finish true hoac sau 1 vong chay ma work khong thay đoi ( khong co tien trinh nao duoc cap thi ) thoat
            break

    if(all(Finish) == False):
        print('He khong an toan',Finish)
    else:
        print('He an toan ',Finish)
# Main
All , Max , Avai , Need , Finish , soTienTrinh= NhapDuLieu()
Work = Avai
XetHeAnToan(All , Need , Work , Finish ,soTienTrinh)





