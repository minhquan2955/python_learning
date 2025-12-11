MOD = 1e9 + 7
n = int(input())
numbers = list(map(int,input().split()))
tong = sum(numbers) % MOD
tich = 1
for x in numbers:
    tich *= x
    tich %= MOD
print(f"{int(tong)} {int(tich)}")