# 17245
# 시간초과 나는 걸로 봐선, 단순 반복문으로 풀면 안된다.
# 그럼 이진 탐색으로? L==1, R==10,000,000 을 초기값으로 탐색하는 것?
input = __import__('sys').stdin.readline
n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
sm = 0
mx = 0
for i in range(n):
    for j in range(n):
        sm += li[i][j]
        mx = max(mx, li[i][j])
left = 0
right = mx
temp = [] # 조건에 만족하는 경우를 모두 저장해두고, 여기서 min값을 뽑으면 될 듯 !
while left <= right:
    mid = (left + right) // 2
    ans = 0
    for i in range(n):
        for j in range(n):
            if li[i][j] >= mid:
                ans += mid
            else:
                ans += li[i][j]
    if sm/2 > ans: # sm/2 <= ans을 찾는 게 목표
        left = mid + 1
    else:
        temp.append(mid)
        right = mid - 1
print(min(temp))


#### 틀린 답 ####
# # 17245
# input = __import__('sys').stdin.readline
# n = int(input())
# li = []
# for i in range(n):
#     li.append(list(map(int,input().split())))
# sm = 0
# for i in range(n):
#     for j in range(n):
#         sm += li[i][j]
# temp = 0
# ans = 0
# while sm/2 > temp:
#     for i in range(n):
#         for j in range(n):
#             if li[i][j] != 0:
#                 li[i][j] -= 1
#                 temp += 1
#     ans += 1
# print(ans)