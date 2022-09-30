# 14754
# heights are all different.
# deque를 이용해서 인덱스를 저장해두기? + 방문체크

input = __import__('sys').stdin.readline
n, m = map(int,input().split())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
ans = []
for i in range(n):
    ans.append(max(li[i]))

for j in range(m):
    temp = []
    for i in range(n):
        temp.append(li[i][j])
    temp = sorted(temp)
    if temp[-1] not in ans:
        ans.append(temp[-1])

res = 0
for i in range(n):
    for j in range(m):
        res += li[i][j]
print(res-sum(ans))

