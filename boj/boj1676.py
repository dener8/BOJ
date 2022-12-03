# 1676
input = __import__('sys').stdin.readline
n = int(input())
res = 1
for i in range(n):
    res *= (i+1)
res = str(res)
ans = 0
for i in range(len(res)-1, -1, -1):
    if res[i] != '0':
        break
    if res[i] == '0':
        ans += 1
print(ans)
