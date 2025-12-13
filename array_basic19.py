n = int(input())
numbers = [int(x) for x in input().split()]
numbers.reverse()
for x in numbers:
    print(x, end=" ")