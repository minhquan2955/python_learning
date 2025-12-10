n = int(input())
numbers = list(map(int,input().split()))
cnt = 0
min_number = 99999999
for x in numbers:
    if x < min_number:
        min_number = x
        cnt = 1
    elif x == min_number:
        cnt += 1
print(cnt)