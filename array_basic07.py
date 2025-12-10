n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
ans = 1e18
for i in range(0,n-1):
    ans = min(ans,abs(numbers[i] - numbers[i+1]))
print(ans)