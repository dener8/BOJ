# 14467
input = __import__('sys').stdin.readline
n = int(input())
dict = {}
cnt = 0
for i in range(n):
    a, b = map(int,input().split())
    if a not in dict:
        dict[a] = b
    else:
        if dict[a] != b:
            dict[a] = b
            cnt += 1
print(cnt)


