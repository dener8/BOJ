# 2343
# 이진탐색
# 블루레이의 크기를 최소로. ex. 15, 16, 17이면 답은 17 (크기가 같아야 함)
# cnt 변수 필요할 , 먼저 1 올리고 시작
# 최댓값이 가장 작게 만들어야 함
# 각 강의의 시간이 배열로 주어짐
# '순서대로' 키워드

input = __import__('sys').stdin.readline
n, m = map(int,input().split())
li = list(map(int,input().split()))
left = max(li)  # 1로 두면 안되나?
right = sum(li)
while left <= right:
    mid = (left+right) // 2
    # print(mid) # mid 로그 찍어보기
    cnt = 0
    temp = 0
    # for i in range(len(li)):
    #     temp += li[i]
    #     if temp > mid:
    #         temp = li[i]
    #         cnt += 1
    # if temp > mid: ### 여기가 문제인 듯 !
    #     cnt += 1
    for i in range(n):
        if temp + li[i] > mid:
            cnt += 1
            temp = 0
        temp += li[i]
    if temp:
        cnt += 1
    if cnt <= m:
        ans = mid
        right = mid - 1
    elif cnt > m:
        left = mid + 1
print(ans)

# 수정하다가 코드가 상당히 더러워졌다.. 다시 리뷰할 것