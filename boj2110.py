# 2110
# 가능한 값의 리스트에서 최솟값이 가장 크게 만들어야 함 (최대한 뭉쳐있어라 이거네)
input = __import__('sys').stdin.readline
n, m = map(int,input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

left = 1
right = house[-1] - house[0]
ans = []
while left <= right:
    mid = (left+right) // 2
    temp = []
    cri = house[0]
    cnt = 1
    for i in range(1, n):
        if house[i] - cri >= mid:
            cnt += 1
            cri = house[i]
    if cnt >= m:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)

# 오답 코드 #

# input = __import__('sys').stdin.readline
# n, m = map(int,input().split())
# house = []
# for _ in range(n):
#     house.append(int(input()))
# house.sort()
#
# left = 1
# right = house[-1] - house[0]
# ans = []
# if m == 2:
#     print(right)
# else:
#     while left <= right:
#         mid = (left+right) // 2
#         temp = []
#         cri = house[0]
#         for i in range(1, n):
#             if house[i] - cri >= mid:
#                 temp.append(house[i] - cri)
#                 cri = house[i]
#         if len(temp) == m-1:
#             ans.append(min(temp))
#             left = mid + 1
#         elif len(temp) > m-1:
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(max(ans))


