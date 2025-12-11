n = int(input())
numbers = [int(x) for x in input().split()]
max_num = max(numbers)
second_max_num = -1
cnt = 0 # dem so lan xuat hien max_num
for x in numbers:
    if x != max_num:
        second_max_num = max(x,second_max_num)
    else:
        cnt += 1
if(cnt > 1):
    second_max_num = max_num
print(f"{max_num} {second_max_num}")