# 20922
# right == n이면 반복문 종료
# dict을 활용.
# dict[right] == k일 경우에 그 때의 길이를 저장하고 dict[right] -= 1
# 그 때 left는 +=1 해준다 // 물론 dict[left] -= 1 도 해줘야겠지
from collections import defaultdict
input=__import__('sys').stdin.readline
n,k=map(int,input().split())
li=list(map(int,input().split()))
left, right = 0, 0
dd = defaultdict(int)
ans = 0
while True:
    if right == n:
        break
    if dd[li[right]] < k:
        dd[li[right]] += 1
        right += 1
    else:
        dd[li[left]] -= 1
        left += 1
    ans = max(right-left, ans)
print(ans)

