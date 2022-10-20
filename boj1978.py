# 1978
input = __import__('sys').stdin.readline
n = int(input())
li = list(map(int,input().split()))
cnt = 0
for i in range(n):
    temp = 0
    for j in range(1, li[i]+1):
        if (li[i] % j) == 0:
            temp += 1
    if temp == 2:
        cnt += 1
print(cnt)