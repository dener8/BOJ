# 2531 / 15961
# k개 연속 선택 경우 할인
# [0]*(n+1) 리스트 생성 => 하나씩 넣고 빼면서 0이 아닌 것 개수 측정
# 예를 들어, [0,0,0,1,2,0] 이라고 치면 ans = 2가 나와야 한다. (0이 아닌 원소 2개)
# 근데 이걸 매번 반복문을 돌려서 확인하면, 30000 * 3000 = 90,000,000의 시간 복잡도가 나온다.
# 통과는 할 수 있겠으나, 좋은 답이라고는 할 수 없을 듯..
# + 아니다 안된다! 회전 초밥이므로, 원래 생각했던 리스트 길이의 *2를 해줘야 한다.
## 위와 번외로, 일단 보너스 초밥의 값을 리스트에 넣어두고 생각하는 것이 좋음!

from collections import defaultdict
input = __import__('sys').stdin.readline
n, d, series, coupon = map(int,input().split())
sushi = []
for i in range(n):
    sushi.append(int(input()))
sushi = sushi * 2
dd = defaultdict(int)
left, right = 0, 0 # right도 0으로 시작하는 문제가 많은 듯
ans = 0
dd[coupon] += 1 # 보너스 초밥 미리 넣어두기
# dd[sushi[0]] += 1 # 첫 번째 원소 넣어두기 => 이런 예외처리를 뺄 수 있는 코드를 생각하자!!
while True:
    if right == series:
        break
    dd[sushi[right]] += 1
    right += 1

while True:
    if right == n*2:
        break
    if right-left == series:
        ans = max(len(dd), ans)
        dd[sushi[left]] -= 1
        if dd[sushi[left]] == 0:
            del dd[sushi[left]]
        left += 1
        dd[sushi[right]] += 1
        right += 1
    else:
        dd[sushi[right]] += 1
        right += 1

print(ans)
