# 9372
# 어디서 출발해야 한다는 말이 없고, 연결 그래프이므로
# [노드 개수 - 1]을 출력해주면 된다.
# 왕복 비행기 => a->b 와 b->a의 비행기가 같은 종류임을 의미함
input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    for i in range(m):
        a, b = map(int,input().split())
    print(n-1)