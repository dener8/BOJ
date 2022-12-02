# 2217
input = __import__('sys').stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li = sorted(li, reverse=True)
mx = 0
for i in range(len(li)):
    mx = max(mx, li[i] * (i+1))
print(mx)