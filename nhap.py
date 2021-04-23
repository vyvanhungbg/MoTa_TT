import numpy as np
import  sys
def NhapMaTran(soTienTrinh): #  n là số tiến trình  s
    List = []
    for i in range(0,soTienTrinh):
        List.append(list(map(int,input().split())))
    return np.array(List)

def NhapDuLieu(): # nhap m so trên 1 dòng
    soTienTrinh = int(input('Nhap so tien trinh  : '))
    print('Nhap Allocation : ')
    All = NhapMaTran(soTienTrinh)
    print('Nhap Max : ')
    Max = NhapMaTran(soTienTrinh)
    print('Nhap Available 1 dong : ')
    Avai = NhapMaTran(1)[0] # [0] là chuyển về ma tran 1x1
    Need = Max - All

    return All , Max , Avai, Need ,soTienTrinh

def XetHeAnToan(All, Need , Avai,soTienTrinh):
    Finish = [False for i in range(0, soTienTrinh)]
    Work = np.copy(Avai)
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
        return 0
    else:
        print('He an toan ',Finish)
        print("Work :")
        print(Work)
        return 1

def YeuCauThem(All, Need , Avai ,soTienTrinh):
    alloc = np.copy(All)
    need = np.copy(Need)
    avai = np.copy(Avai)

    list_p = list(map(int,input("Nhap cac tien trinh yeu cau them tai nguyen P[?] lan luot: ").split()))
    listRequest = []
    for p in list_p:
        listRequest.append(list(map(int,input("Nhap Request["+str(p)+"] : \n").split())))
    listRequest = np.array(listRequest)

    sum_alloc_request = [0 for i in range(0,len(avai))]# khoi tao bien tong tat ca cac request bang 0
    for p,request_p in  zip(list_p,listRequest):
        if all( need[p] >=  request_p ) == False:
            print("Request[" +str(p)+ "] la khong hop le , ket thuc ! : ")
            return
        sum_alloc_request += request_p

    if all(sum_alloc_request <= avai ) == False :
            print(" Khong dap ung du tong so luong request , ket thuc !  : ")
            return
    # cap nhat lai sau khi gia dinh dap ung cac request
    for p,request_p in  zip(list_p,listRequest):
        alloc[p] += request_p
        need[p]-= request_p
        avai -= request_p

    if XetHeAnToan(alloc , need , avai ,soTienTrinh):
        print("Phan bo tai nguyen cho cac request !")
    else :
        print("Khong phan bo tai nguyen cho cac request !")

# Main
All , Max , Avai , Need  , soTienTrinh= NhapDuLieu()

while True:
    print("Chon  1 de Xet he an toan")
    print("Chon  2 de Request them ")
    print("Chon  3 de xuat Need , Alloc , Avail")
    print("Chon  0 de thoat !")
    chon = int(input("Chon : "))
    if chon ==1 :
        XetHeAnToan(All, Need, Avai, soTienTrinh)
    elif chon == 2 :
        YeuCauThem(All, Need, Avai, soTienTrinh)
    elif chon == 0 :
        sys.exit(0)
    elif chon == 3:
        print("Aloc : ")
        print(All)
        print("Need")
        print(Need)
        print("Avai")
        print(Avai)
    else:
        pass







