# 1120
input = __import__('sys').stdin.readline
a, b = input().split()
mn = 50
for j in range(len(b) - len(a) + 1):
    temp = 0
    for i in range(len(a)):
        if a[i] != b[i+j]:
            temp += 1
    mn = min(temp, mn)
print(mn)