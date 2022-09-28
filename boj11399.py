# 11399
input = __import__('sys').stdin.readline
n = int(input())
li = list(map(int,input().split()))
li.sort()
ans = 0
for i in range(1, len(li)+1):
    ans += sum(li[:i])
print(ans)