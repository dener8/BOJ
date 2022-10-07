# 4307
input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    li = []
    for i in range(m):
        li.append(int(input()))
    li.sort()
    temp = []
    for i in range(len(li)):
        temp.append(min(li[i], n-li[i]))
    mn = max(temp)
    mx = max(n-li[0], li[-1])
    print(mn, mx)