# 2805
# 가능한 높이의 범위 중 하나를 정하고 => mid (left == 1, right == max값)
# mid로 다 잘라냈을 때 값이 m 이상인지를 골라내면 된다.
# m과 동일하면 최적의 값이지만, 그렇지 않은 경우도 대비해야 함! 결과들을 리스트에 담고 가장 큰 값을 출력해주면 되겠네
input = __import__('sys').stdin.readline
n, m = map(int,input().split())
li = list(map(int,input().split()))
left = 1
right = max(li)
able = []
while left <= right:
    cut = 0
    mid = (left+right) // 2
    for i in li:
        if i > mid:
            cut += i - mid
    if cut > m: # 잘라낸 것 > 최소치 => 덜 잘라낼 수 있게 mid를 올려줘야 한다.
        left = mid + 1
        able.append(mid)
    elif cut < m:
        right = mid - 1
    else:
        able.append(mid)
        break
if able:
    print(max(able))
else:
    print(0)