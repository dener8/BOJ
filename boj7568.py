# 7568
input = __import__('sys').stdin.readline
n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
ans_li = []
for i in range(n):
    weight, height = li[i][0], li[i][1]
    ans = 1
    for j in range(n):
        if weight < li[j][0] and height < li[j][1]:
            ans += 1
    ans_li.append(ans)
print(*ans_li)
