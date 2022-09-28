# 11047
input = __import__('sys').stdin.readline
n, k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
ans = 0
i = 0
while k > 0:
    if k // coin[i]:
        ans += k // coin[i]
        k = k % coin[i]
    i += 1
print(ans)