# 13335
from collections import deque
input = __import__('sys').stdin.readline
n, w, L = map(int,input().split())
dq = deque(list(map(int,input().split())))
bridge = deque([0]*w)
ans = 0
while dq:
    ans += 1
    bridge.popleft()
    if sum(bridge) + dq[0] <= L:
        x = dq.popleft()
        bridge.append(x)
    else:
        bridge.append(0)
print(ans + w)

# 문제풀이
'''
"1. 다리를 건넌 후/ 2. 다리 위/ 3. 다리를 건너기 전"
이렇게 세 부분으로 나누어 생각해 볼 수 있다.
각각의 배열을 만들어야 하는데, 들어온 방향과 반대 방향으로 나가야 하므로 deque을 사용했다.
하지만 '2'와 '3'의 트럭이 담긴 deque에 없는 것은 다리를 다 건넌 것으로 판단할 수 있으므로, '1'을 나타내는 deque은 구현하지 않았다.
원소가 0이고 길이가 w인 deque에 원소를 넣고 빼는 과정을 진행해주면 된다.
'3'의 길이가 0일 때까지 while문을 돌리고, 매 시행마다 ans을 1씩 증가시킨다.
매 시행마다 '2'에서 원소가 하나씩 pop되는 것도 default이다.
'3'의 가장 첫번 째 원소와 다리에 놓여있는 트럭 무게들의 합을 제한 무게인 L과 비교하여 새로운 트럭을 넣을지 말지 결정해주면 된다.
while문이 종료되면, '3'에는 원소가 없는 상태고 마지막 트럭이 '2'의 가장 끝에 담겨있을 것이므로, ans에 다리 길이인 w를 합한 결과를 출력해주면 끝.
'''
# 메모
'''
'2. 다리 위'의 초기 상태를 원소가 0이고 길이가 w인 배열로 설정하는 것을 바로 생각해냈다면 금방 풀었겠지만, 그걸 생각하지 못해서 꽤 오래 걸렸다.
처음에는 원소가 없는 빈 deque으로 시작할 생각이었지만, 전술한 방법이 훨씬 간단하다.
투포인터로도 가능하지 않을까 생각했지만, 쉬운 방법을 우선적으로 생각하는걸로ㅎㅎ..
'''






