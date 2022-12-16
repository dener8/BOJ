# 2847
input = __import__('sys').stdin.readline
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
ans = 0
for i in range(1, n):
    while li[-i] <= li[-i-1]:
        li[-i-1] -= 1
        ans += 1
print(ans)



