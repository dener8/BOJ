# 2953
input = __import__('sys').stdin.readline
li = []
for i in range(5):
    li.append(list(map(int,input().split())))
ans = []
for i in range(5):
    ans.append(sum(li[i]))
ansScore = max(ans)
for i in range(5):
    if ans[i] == ansScore:
        print(i+1, ansScore)
