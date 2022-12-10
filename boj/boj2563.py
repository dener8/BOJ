# 2563
input = __import__('sys').stdin.readline
total = [[0]*100 for _ in range(100)] # 총 10,000개의 셀로 생각하기
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            total[i][j] = 1
ans = 0
for i in range(len(total)):
    ans += sum(total[i])
print(ans)