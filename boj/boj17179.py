# 17179
# 오름차순: 정렬된 상태 -> O(logN)
input = __import__('sys').stdin.readline
n, m, l = map(int, input().split())
spot = []
for _ in range(m):
    spot.append(int(input()))
spot.append(l) # 마지막까지 넣어두는 과정 필요할 듯
pieces = []
for _ in range(n):
     pieces.append(int(input()))

# 결국 여러 개 중 최솟값이 기준이 되어야하니까, 이것보다 크거나 같은 것만 가능하지
for piece in pieces:
    left = 0
    right = 4000001

    while left <= right:
        mid = (left + right) // 2
        val = 0
        ans = 0
        for i in range(len(spot)):
            gap = spot[i] - val
            if gap >= mid:
                ans += 1
                val = spot[i]
            elif gap < mid:
                continue

        if ans >= piece + 1:
            left = mid + 1
        elif ans < piece + 1:
            right = mid - 1
    print(right)

'''
pieces 리스트는 논외로 생각해보면,
left = 0 right = 4000000으로 설정해서 케이크의 최소크기를 맞추면 되지 않을까?
'''