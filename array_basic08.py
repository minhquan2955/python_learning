n = int(input())
numbers = list(map(int,input().split()))
ds = dict()
for i in range(0,n):
    ds[numbers[i]] = i
for x in ds:
    print(x, end=" ")