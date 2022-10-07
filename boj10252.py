# 10252
input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    cnt = 0
    print(1)
    for i in range(m-1, -1, -1):
        print('('+'0'+','+str(i)+')')
    while cnt < m:
        if cnt % 2 == 0:
            for i in range(1, n):
                print('('+str(i)+','+str(cnt)+')')
        else:
            for i in range(n-1, 0, -1):
                print('('+str(i)+','+str(cnt)+')')
        cnt += 1