# 14490

# # 1. 라이브러리 사용
# import math
# n, m = map(int, input().split(':'))
# gcd = math.gcd(n, m)
# print(n // gcd, m // gcd, sep = ':')

# 2. 라이브러리 사용 X
def gcd(n, m):
    bigger = max(n, m)
    gcdVal = 0
    for i in range(1, bigger + 1):
        if not n % i and not m % i:
            gcdVal = i
    return gcdVal

n, m = map(int, input().split(':'))
gcdVal = gcd(n, m)
print(n // gcdVal, m // gcdVal, sep = ':')