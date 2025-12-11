# list = [none] * n: list n phần tử none
fibs = set()
f0 = 0
f1 = 1
fibs.add(f0)
fibs.add(f1)
for i in range(2,93):
    temp = f1 + f0
    f1, f0 = temp, f1
    fibs.add(f1)
n = int(input())
numbers = list(map(int,input().split()))
check = True
for x in numbers:
    if x in fibs:
        check = False
        print(x, end=" ")
if check:
    print("NONE")