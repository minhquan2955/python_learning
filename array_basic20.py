n = int(input())
numbers = list(map(int,input().split()))
for i in range(1,n-1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        print(numbers[i], end=" ")