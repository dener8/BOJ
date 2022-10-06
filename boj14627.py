# 14627
# 하나 이상의 파가 들어가면 안됨 => right == min(li)-1 로 설정해야하지 않을까?
#
input = __import__('sys').stdin.readline
n, m = map(int,input().split())
li = []
for _ in range(n):
    li.append(int(input()))
left = 1
right = max(li)
while left <= right:
    mid = (left + right) // 2
    temp = 0
    extra = 0
    for i in range(n):
        temp += li[i] // mid
        # extra += li[i] % mid # extra == 남은 파들의 모임
    if temp >= m:
        left = mid + 1 # 파의 길이를 늘려줘야 함
        res = mid # 이걸 안쓰고 최종 출력에 res가 아닌 mid를 쓰면 왜 안되는가
    else:
        right = mid - 1
if m == 1:
    print(0)
else:
    print(sum(li) - m * res)