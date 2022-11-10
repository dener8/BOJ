# 1755
input = __import__('sys').stdin.readline
m, n = map(int, input().split())
numOrder = [8, 5, 4, 9, 1, 7, 6, 3, 2, 0]
res = []
for i in range(len(numOrder)-1):
    res.append(numOrder[i])
    for j in range(len(numOrder)):
        num = int(str(numOrder[i]) + str(numOrder[j]))
        res.append(num)
li = [i for i in range(m, n+1)]
cnt = 0
ans = []
for i in range(len(res)):
    if (res[i] in li):
        ans.append(res[i])
for i in range(len(ans) // 10 + 1):
    print(' '.join(map(str, ans[10*i:10*i+10])))