# 13417
from collections import deque
input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    ori = deque(list(input().rstrip().split()))
    q = deque()
    for i in range(len(ori)):
        if len(q)==0:
            q.append(ori[i])
        else:
            if ord(ori[i]) > ord(q[0]) :
                q.append(ori[i])
            else:
                q.appendleft(ori[i])
    print(''.join(q))



