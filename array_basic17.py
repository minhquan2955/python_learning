n = int(input())
numbers = [int(x) for x in input().split()]
if numbers == numbers[::-1]:
    print("YES")
else:
    print("NO")