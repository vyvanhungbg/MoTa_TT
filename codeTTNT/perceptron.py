import  numpy as np
import  math
list_p = np.array([[0, 2], [1, 0], [0, -2], [2, 0]])
list_t = np.array([1,1,0,0])

w = np.array([-1, 2])
b= 1
list_check = [False for i in range(0,len(list_t))]

def setCheck(index):
    for i in range(0,len(list_check)):
        list_check[i] = False
    list_check[index] = True

def hl(n):
    if n >= 0:
        return 1
    return 0
def pl(n):
    return n

def logsign(n):
    return 1+ math.exp(-n)


def tinhN(w,p,b):
    return np.dot(w, p.T) + b

loop = 1
while all(list_check) == False:

    print("\nXet lan lap ",loop)
    for i in range(0,len(list_t)):
        n = tinhN(w, list_p[i], b)
        a = hl(n)

        if a == list_t[i]:
            print("Xet p["+str(i+1)+"] giu nguyen vi co n = "+str(n) +" tinh a = ",a)
            print("\tGiu nguyen trong so")
            list_check[i] = True
        else:
            w = w + (list_t[i] - a) * list_p[i]
            b = b + (list_t[i] - a)
            print("Xet p["+str(i+1)+"] cap nhat trong so vi co n = "+str(n) +" tinh a = ",a)
            print("\tw = ",w)
            print("\tb = ",b)
            setCheck(i)
    loop += 1

print("\nKQ , w = ",w)
print("KQ , b = ",b)