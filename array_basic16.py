import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def thuan_nghich(n):
    temp = str(n)
    return temp == temp[::-1]
def chinh_phuong(n):
    x = int(math.sqrt(n))
    return x * x == n
def tong_chu_so(n):
    tong = 0
    while(n != 0):
        tong += int(n % 10) #ep kieu int do '%' tra ve float => tong se la float => snt(tong) se loi
        n /= 10
    return snt(tong)
n = int(input())
numbers = list(map(int,input().split()))
cnt1, cnt2, cnt3, cnt4 = 0,0,0,0
for x in numbers:
    if snt(x):
        cnt1 += 1
    if thuan_nghich(x):
        cnt2 += 1
    if chinh_phuong(x):
        cnt3 += 1
    if tong_chu_so(x):
        cnt4 += 1
print(f"{cnt1}\n{cnt2}\n{cnt3}\n{cnt4}")