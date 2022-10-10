# 1543
input = __import__('sys').stdin.readline
a = input().rstrip()
b = input().rstrip()
i = 0
cnt = 0
while i <= len(a)-len(b):
    if a[i:i+len(b)] == b:
        cnt += 1
        i += len(b)
    else:
        i += 1
print(cnt)