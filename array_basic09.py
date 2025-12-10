from collections import Counter
n = int(input())
numbers = [int(x) for x in input().split()]
ds = Counter(numbers)
for k in ds:
    print(f"{k} {ds.get(k)}") #ds[k]
