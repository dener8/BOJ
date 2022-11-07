# 1026
input = __import__('sys').stdin.readline
n = int(input())
listA = sorted(list(map(int,input().split())), reverse=True)
listB = sorted(list(map(int,input().split())))

ans = 0
for i in range(n):
    ans += listA[i] * listB[i]
print(ans)
