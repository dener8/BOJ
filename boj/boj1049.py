# 1049
input = __import__('sys').stdin.readline
n, m = map(int, input().split())
packMin = 1000 # 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
eachMin = 1000
for i in range(m):
    a, b = map(int, input().split())
    packMin = min(packMin, a)
    eachMin = min(eachMin, b)

ans = 1000 * 100
for i in range(n+1):
    temp = eachMin * i + ((n-i-1) // 6 + 1) * packMin
    ans = min(ans, temp)
print(ans)