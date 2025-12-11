'''
Docstring for array_basic14
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, int(a%b))

'''

import math
n = int(input())
numbers = list(map(int,input().split()))
if len(numbers) == 1:
    print(numbers[0])
else:
    x = math.gcd(numbers[0],numbers[1])
    for i in range(2,n):
        temp = math.gcd(numbers[i],x)
        x = temp
    print(x)


