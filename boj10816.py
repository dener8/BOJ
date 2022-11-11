# 10816
from collections import defaultdict
dd = defaultdict(int)
input = __import__('sys').stdin.readline
n = int(input())
li = list(map(int, input().split()))
m = int(input())
temp = list(map(int, input().split()))
for i in range(len(temp)):
    if (dd[temp[i]] == 0):
        dd[temp[i]] += 1
for i in range(len(li)):
    dd[li[i]] += 1
for i in range(len(temp)):
    print(dd[temp[i]] - 1, end=' ')

# 같은 카드를 또 물어볼 수도 있다!