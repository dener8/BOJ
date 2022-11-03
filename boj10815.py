# 10815
from collections import defaultdict
input = __import__('sys').stdin.readline
dd = defaultdict(int)
n = int(input())
listA = list(map(int,input().split()))
for i in range(len(listA)):
    dd[listA[i]] += 1
n = int(input())
listB = list(map(int,input().split()))
for i in range(len(listB)):
    if (dd[listB[i]]):
        print(1, end=' ')
    else:
        print(0, end=' ')