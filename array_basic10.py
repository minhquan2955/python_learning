
'''
map(func,list): ap dung func cho tung phan tu cua list, nhưng chỉ lưu trạng thái(ko lưu kq lưu dài, tức: sau khi duyệt for qua 1 lần thì lần sau trở thành rỗng)
tra ve Map Object(ban chat la 1 iterator: chay qua tung phan tu cua list va chi ap dung func khi no dc dung den(thong qua for hoac ham next(),...))
numbers = [1, 2, 3]
m = map(int, numbers)

Lần 1: Chạy OK
print(list(m)) # Output: [1, 2, 3]

Lần 2: Chạy lại trên biến m cũ
print(list(m)) # Output: []  <-- RỖNG!

 '''
import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int,input().split()))
for i in range(1,n-1):
    #numbers[start:end]: subarray(start->end-1)
    if snt(sum(numbers[0:i])) and snt(sum(numbers[i+1:n])):
        print(i, end=" ")