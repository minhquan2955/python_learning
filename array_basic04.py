n = int(input())
numbers = list(map(int,input().split())) # input().split() chinh la 1 list
x = int(input())
cnt1,cnt2 = 0,0
for num in numbers:
    if num < x:
        cnt1 += 1
    elif num > x:
        cnt2 += 1
print(f"{cnt1}\n{cnt2}")