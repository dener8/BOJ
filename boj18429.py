# 18429
'''
하루 1개의 키트만 사용 가능 (키트도 각각 1개씩만 있다.)
항상 500이상 유지
'''

input = __import__('sys').stdin.readline
cnt = 0
n, k = map(int,input().split())
kit = list(map(int,input().split()))
visited = [0] * n

def go(depth, weight):
    global cnt
    if (depth == n):
        cnt += 1
        return
    for i in range(len(kit)):
        if (not visited[i]) and (weight - k +  kit[i] >= 500):
            visited[i] = 1
            go(depth + 1, weight - k + kit[i])
            visited[i] = 0

go(0, 500)
print(cnt)
