n = int(input())
numbers = [int(x) for x in input().split()] # list comprehension
# numbers = list(map(int,input().split()))
check = False
for i in range(0,n):
    if(i % 2 == 0 and numbers[i] % 2 == 0):
        print(numbers[i], end=" ")
        check = True
if check is False:
    print("NONE")
