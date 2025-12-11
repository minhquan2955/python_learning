n = int(input())
numbers = [int(x) for x in input().split()]
min_num = min(numbers)
max_num = max(numbers)
max_i = -1
min_i = 1e18
for i, x in enumerate(numbers): #enumerate(list): duyet dong thoi (index,value)
    if(x == max_num):
        min_i = min(min_i,i)
    elif(x == min_num):
        max_i = max(max_i,i)
print(f"{max_i} {min_i}")