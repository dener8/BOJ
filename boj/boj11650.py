# 11650
input = __import__('sys').stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))
li = sorted(li, key=lambda x: [x[0], x[1]])
for i in range(n):
    print(li[i][0], li[i][1])