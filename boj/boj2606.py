# 2606
input = __import__('sys').stdin.readline
n = int(input())
li = [[0]*(n+1) for _ in range(n+1)] # 행렬 기준으로 첫 행과 첫 열은 비워두기 (1부터 시작하는 편의성을 위해)
chk = [0]*(n+1)
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    li[a][b] = 1
    li[b][a] = 1

def go(idx):
    for i in range(1, n+1):
        if li[idx][i] == 1 and chk[i] == 0:
            chk[i] = 1
            go(i)

chk[1] = 1 # 첫 시작이므로 무조건 방문
go(1)
print(sum(chk)-1) # 1번 컴퓨터는 빼주기

