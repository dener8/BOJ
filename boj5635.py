# 5635
input = __import__('sys').stdin.readline
n = int(input())
li = []
for i in range(n):
    temp = list(input().rstrip().split())
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    li.append(temp)
li = sorted(li, key = lambda x: [x[3], x[2], x[1]])
print(li[-1][0])
print(li[0][0])
