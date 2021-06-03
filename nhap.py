from warnings import catch_warnings

import numpy as np
import sys


def NhapMaTran(soTienTrinh):  # n là số tiến trình  s
    List = []
    for i in range(0, soTienTrinh):
        List.append(list(map(int, input().split())))
    return np.array(List)


def NhapDuLieu():  # nhap m so trên 1 dòng
    soTienTrinh = int(input('Nhap so tien trinh  : '))
    print('Nhap Allocation : ')
    All = NhapMaTran(soTienTrinh)
    print('Nhap Max : ')
    Max = NhapMaTran(soTienTrinh)
    print('Nhap Available 1 dong : ')
    Avai = NhapMaTran(1)[0]  # [0] là chuyển về ma tran 1x1
    Need = Max - All
    return All, Max, Avai, Need, soTienTrinh


def XetHeAnToan(All, Need, Avai, soTienTrinh):
    Finish = [False for i in range(0, soTienTrinh)]  # khoi tao Finish[i] = False voi i = ...
    Work = np.copy(Avai)
    list_tien_trinh= []
    while True:
        i = 0
        while i < soTienTrinh:
            WorkLucDau = np.copy(Work)
            if all(Need[i] <= Work) == True and Finish[i] == False: # thoa man th tien trinh duoc chay va khong phai cho
                list_tien_trinh.append(i)
                Work += All[i]
                Finish[i] = True
            i += 1
        if all(Finish) or (Work == WorkLucDau).all():  # neu ma tat ca Finish true hoac sau 1 vong chay ma work khong thay đoi ( khong co tien trinh nao duoc cap thi ) thoat
            break

    if all(Finish) == False:
        #print("Thu tu tien trinh duoc phan bo ",list_tien_trinh)
        return 0  # print('He khong an toan',Finish)
    else:
        print("Thu tu tien trinh duoc phan bo ", list_tien_trinh)
        return 1



def YeuCauThem(All, Need, Avai, soTienTrinh):
    alloc = np.copy(All)
    need = np.copy(Need)
    avai = np.copy(Avai)

    list_p = list(map(int, input("Nhap cac tien trinh yeu cau them tai nguyen P[?] lan luot: ").split()))
    listRequest = []
    for p in list_p:
        listRequest.append(list(map(int, input("Nhap Request[" + str(p) + "] : \n").split())))
    listRequest = np.array(listRequest)

    sum_alloc_request = [0 for i in range(0, len(avai))]  # khoi tao bien tong tat ca cac request bang 0
    for p, request_p in zip(list_p, listRequest):
        if not all(need[p] >= request_p):
            print("Khong phan bo tai nguyen cho cac request !, ( Request[" + str(p) + "] la khong hop le )")
            return 0
        sum_alloc_request += request_p

    if not all(sum_alloc_request <= avai):
        print("Khong phan bo tai nguyen cho cac request !, ( Loi khong dap ung du tong so luong request ) ")
        return 0
    # cap nhat lai sau khi gia dinh dap ung cac request
    for p, request_p in zip(list_p, listRequest):
        alloc[p] += request_p
        need[p] -= request_p
        avai -= request_p

    if XetHeAnToan(alloc, need, avai, soTienTrinh):
        print("Phan bo tai nguyen cho cac request ! p[i] = ", list_p)
    else:
        print("Khong phan bo tai nguyen cho cac request ! ")

# Main
All, Max, Avai, Need, soTienTrinh = NhapDuLieu()

while True:
    print("\n------------------\nChon  1 de Request them ")
    print("Chon  0 de thoat !")
    chon = int(input("Chon : "))
    if chon == 1:
        YeuCauThem(All, Need, Avai, soTienTrinh)
    elif chon == 0:
        sys.exit(0)
    else:
        pass
