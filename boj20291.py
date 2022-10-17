# 20291
from collections import defaultdict
input = __import__('sys').stdin.readline
dd = defaultdict(int)
n = int(input())
for _ in range(n):
    s = input()
    for i in range(len(s)):
        if s[i] == '.':
            break
    dd[s[i+1:len(s)-1]] += 1
keys = list(dd.keys())
keys.sort()
for i in range(len(keys)):
    print(keys[i], dd[keys[i]])