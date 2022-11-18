# 2108
from collections import defaultdict
input = __import__('sys').stdin.readline
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
li.sort()

# 1. 산술평균
avg = round(sum(li)/n)
print(avg)

# 2. 중앙값
mid = li[n//2]
print(mid)

# 3. 최빈값
dd = defaultdict(int)
most = 0
for i in range(n):
    dd[li[i]] += 1
ans = []
ddKeys = list(dd.keys())

for i in range(len(dd)):
    if most == dd[ddKeys[i]]:
        ans.append(ddKeys[i])
    elif most < dd[ddKeys[i]]:
        ans = [ddKeys[i]]
        most = dd[ddKeys[i]]
if len(ans) == 1:
    print(ans[0])
else:
    ans.sort()
    print(ans[1])

# 4. 범위
gap = li[-1]-li[0]
print(gap)