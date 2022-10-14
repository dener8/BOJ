# 5567
from collections import deque
input = __import__('sys').stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
chk = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
q = deque()
chk[1] = 1
for i in range(len(graph[1])):
    q.append(graph[1][i])
    chk[graph[1][i]] = 1
    cnt += 1
while q:
    x = q.popleft()
    for i in range(len(graph[x])):
        if chk[graph[x][i]] == 0:
            chk[graph[x][i]] = 1
            cnt += 1
print(cnt)
