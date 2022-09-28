# # 1940
# input = __import__('sys').stdin.readline
# n = int(input())
# m = int(input())
# li = list(map(int,input().split()))
# li.sort()
# left, right = 0, n-1
# ans = 0
# while True:
#     if left == right:
#         break
#     sum = li[left] + li[right]
#     if sum == m:
#         ans += 1
#         right -= 1
#         # left += 1
#     elif sum > m:
#         right -= 1
#     else:
#         left += 1
# print(ans)


