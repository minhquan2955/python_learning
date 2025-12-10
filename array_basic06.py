from collections import defaultdict
from collections import Counter
# Dùng Counter cho 99% trường hợp đếm tần suất.
# Dùng defaultdict(int) nếu bạn cần tùy biến logic đếm phức tạp.
n = int(input())
numbers = [int(x) for x in input().split()]
k = int(input())
#ds = defaultdict(int)
ds = Counter(numbers)
#for x in numbers:
    #ds[x] += 1
cnt = 0
for x in ds:
    if k - x in ds:
        cnt += max(ds[x],ds[k-x])
print(cnt)        
