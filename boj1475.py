# 1475
input = __import__('sys').stdin.readline
n = input().rstrip()
li = [0] * 10
for i in range(len(n)):
    li[int(n[i])] += 1
li[6], li[9] = (li[6]+li[9]+1) // 2, (li[6]+li[9]+1) // 2
print(max(li))