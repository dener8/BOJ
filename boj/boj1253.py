# # 1253
# from collections import defaultdict
# input = __import__('sys').stdin.readline
#
# dd = defaultdict(int)
# ddTemp = defaultdict(int)
# n = int(input())
# li = list(map(int, input().split()))
# li.sort()
#
# for i in range(n-1):
#     for j in range(i+1, n):
#         dd[(li[i] + li[j], i, j)] += 1 # 인덱스를 같이 넣어주기 # 이렇게하면 모든 원소 다 들어감
#
# keys = list(dd.keys())
# ans = 0
# idx = 0
# for i in range(len(li)):
#     # for j in keys:
#     #     if i == j[0] and idx != j[1] and idx != j[2]:
#     #         ans += 1
#     #         print(i, j)
#     for j in range(i, len(keys)):
#         if li[i] == keys[j][0] and i != keys[j][1] and i != keys[j][2] and tuple(keys[j]) in dd:
#             ans += 1
#     # idx += 1
# print(ans)
# #
# # keys = dd.keys()
# # ans = 0
# # idx = 0
# # for i in range()

"""
3
0 0 1
예외 케이스; dict으로 하게되면, 자기 자신과의 연산까지 포함하게 된다.
작성한 코드로는 3이 나오지만, 결과는 0이 나와야 한다!
"""
"""
defaultdict으로 푸는 방법이 분명 있을 것 같은데 계속 시도하다가 포기..
다음에 다시 도전해보기!! 
"""
#####################################################################################

# 투 포인터
"""
이 문제는, 두 포인터가 같은 쪽에서 시작하지 않고 반대 쪽에서 시작해야 하는 문제이다.
만약 같은 쪽에서 시작할 경우, 탐색하지 못하는 쌍이 생긴다.
예를 들어,
1 2 3 5 6 7 8 에서 합이 5인 쌍을 찾아야 한다고 했을 때,
1 + 2 < 5 : right 이동
1 + 3 < 5 : right 이동
1 + 5 > 5 : left 이동
2 + 5 > 5 : left 이동
3 + 5 > 5 : left 이동 .. 이런식으로 진행된다.
2 + 3은 만족하는 쌍이지만, 아예 거치지 않는 일이 생긴다.
그러므로 이런 경우에는 두 포인터가 다른 쪽에서 오는 방법을 택해야 한다.
"""

input = __import__('sys').stdin.readline
n = int(input())
li = sorted(list(map(int, input().split())))
ans = 0

for i in range(n): # O(N * N) == 2000 * 2000
    left, right = 0, n-2
    tempList = li[:i] + li[i+1:]
    num = li[i]
    while left != right:
        sumVal = tempList[left] + tempList[right]
        if num == sumVal:
            ans += 1
            break
        elif num > sumVal:
            left += 1
        elif num < sumVal:
            right -= 1
print(ans)














