# 11070
input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    win = [0] * (n+1)
    lose = [0] * (n+1)
    for i in range(m):
        a, b, p, q = map(int,input().split())
        win[a] += p
        win[b] += q
        lose[a] += q
        lose[b] += p
    ans = []
    for i in range(1, n+1):
        if win[i]**2 + lose[i]**2 == 0:
            ans.append(0)
        else:
            ans.append(int((win[i]**2 / (win[i]**2 + lose[i]**2)) * 1000))
    print(max(ans))
    print(min(ans))


