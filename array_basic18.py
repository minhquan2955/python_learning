n = int(input())
numbers = list(map(int,input().split()))
for i in range(0,n):
    if i == 0:
        if numbers[0] * numbers[1] < 0:
            print(numbers[0], end=" ")
    elif i == n - 1:
        if numbers[n-1] * numbers[n-2] < 0:
            print(numbers[n-1])
    else:
        if numbers[i] * numbers[i-1] < 0 or numbers[i] * numbers[i+1] < 0:
            print(numbers[i], end=" ")
            