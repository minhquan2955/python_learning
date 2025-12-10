
n = int(input())
numbers = [int(x) for x in input().split()]
k = int(input())
cnt = 0
for i in range(0,n):
    if numbers[i] <= k:
        for j in range(i+1,n):
            if numbers[j] + numbers[i] == k:
                cnt += 1
print(cnt)
