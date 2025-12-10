import math
def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    tong = 0
    for x in numbers:
        if snt(x):
            cnt += 1
            tong += x
    result = tong / cnt
    print(f"{result:.3f}")

if __name__ == "__main__":
    main()