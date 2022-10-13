# 5800
input = __import__('sys').stdin.readline
n = int(input())
for i in range(1, n+1):
    li = list(map(int,input().split()))
    li = sorted(li[1:])
    mx = 0
    for j in range(len(li)-1):
        mx = max(mx, li[j+1]-li[j])
    print('Class',i)
    print('Max {}, Min {}, Largest gap {}'.format(max(li), min(li), mx))
