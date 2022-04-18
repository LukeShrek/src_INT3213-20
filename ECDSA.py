import math
import random
import sys
# cài đặt thêm libnum (pip3 install libnum)
import libnum

# nhập p đầu vào
print('enter p')
p=int(input())
# định nghĩa kiểu class ecc và ecpoint
class ecc:
    def __init__(self,a,b,p):
        self.a = a
        self.b = b
        self.p = p
class ecpoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# hàm lựa chọn a, b ngẫu nhiên thỏa mãn |a,b| < p và 4a^3+27b^2 != 0 (mod p)
def select_random_number(p):
    a = random.randint(-p,p)
    b = random.randint(-p,p)
    while ((4*(a**3)+27*(b**2)) %p == 0):
        a = random.randint(-p,p)
        b = random.randint(-p,p)
    return a,b
# hàm check số nguyên tố
def isprime(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1
# hàm đếm số điểm theo phương pháp liệt kê
def point_counter(e: ecc):
    # count bằng 1 khởi tạo do tính điểm 0,0 vào đường cong
    count = 1
    for i in range (0,p):
        for j in range (0,p):
            if ((j**2)%e.p == (i**3 + e.a*i + e.b)%e.p):
                count=count+1
    return count
# hàm khởi tạo ngẫu nhiên đường cong
# def generate_curve(p):
#     a,b=select_random_number(p)
#     e=ecc(a,b,p)
#     g=point_counter(e)
#     # nếu số điểm của đường cong không phải số nguyên tố thì tạo lại
#     while(isprime(g) != True):
#         a,b=select_random_number(p)
#         e=ecc(a,b,p)
#         g=point_counter(e)
#     return a,b,g

a,b=10,9
e=ecc(a,b,p)
g=point_counter(e)
print (f"Duong Cong Elliptic: y^2 = x^3 + {a}x + {b} mod {p} co so diem la {g} ")
# Hàm tìm điểm sinh của đường cong vừa tạo
# vì đường cong có số điểm là số nguyên tố nên bất kỳ điểm nào trên đường cong đều là điểm sinh
def find_generator(a,b,p):
    for i in range (0,p):
        for j in range (1,p):
            if ((j**2)%p == (i**3 + a*i + b)%p):
                G=ecpoint(i,j)
                return G

G=find_generator(a,b,p)
print (f"Diem sinh co toa do la ({G.x},{G.y})")

# các hàm cộng điểm và nhân điểm
def point_add(P: ecpoint,Q :ecpoint,E: ecc):
    lamda = (Q.y-P.y)*((Q.x-P.x)**(E.p-2)) % E.p
    xR = (lamda**2 - P.x - Q.x) % E.p
    yR = (lamda*(P.x-xR)-P.y) % E.p
    R = ecpoint(xR,yR)
    return R
def point_double(P: ecpoint,E: ecc):
    #lamda = ((3*(P.x**2)+E.a)*((2*P.y)**(E.p-2))) % E.p
    #xR = (lamda**2 - 2*P.x) % E.p
    #yR = (l.amda*(P.x-xR)-P.y) % E.p
    s=((3*P.x**2)+E.a)  *  libnum.invmod(2*P.y,E.p) 
    x2=(s**2-2*P.x) % E.p
    y2=((s*(P.x-x2))-P.y) % E.p

    R = ecpoint(x2,y2)
    return R

# Tìm tất cả điểm trên đường cong dựa trên điểm sinh trước đó
R=G
S=point_double(R,e)
for i in range (1,g):
    print (f"{i}G = ({R.x},{R.y}) ")
    R=S
    S=point_add(R,G,e)


