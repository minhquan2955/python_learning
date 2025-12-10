n = int(input())
chan,le = 0,0
tong_chan,tong_le = 0,0
number = list(map(int, input().split()))
for x in number:
    if(x % 2 == 0):
        chan += 1
        tong_chan += x
    else:
        le += 1
        tong_le += x
print(f"{chan} \n {le} \n {tong_chan} \n {tong_le}")

