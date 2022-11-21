# 2776
from collections import defaultdict
input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    dd = defaultdict(int)
    n = int(input())
    li = list(map(int,input().split()))
    for i in range(len(li)):
        dd[li[i]] += 1

    m = int(input())
    li = list(map(int,input().split()))
    for i in range(len(li)):
        if (li[i] in dd):
            print(1)
        else:
            print(0)

