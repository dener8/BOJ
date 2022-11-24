# 11256
t = int(input())
for _ in range(t):
    li = []
    j, n = map(int,input().split())
    for i in range(n):
        r, c = map(int, input().split())
        li.append(r*c)
    li.sort()
    ans = 0
    sum = 0
    for i in range(len(li)-1, -1, -1):
        ans += 1
        sum += li[i]
        if sum >= j:
            break
    print(ans)
