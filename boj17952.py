# 17952
# 쌓고 -> 맨 마지막 값에서 1 빼고 -> 맨 위의 것의 맨 마지막이 0이면 아예 pop해버리고.
input = __import__('sys').stdin.readline
n = int(input())
stack = []
score = 0
for i in range(n):
    li = list(map(int,input().split()))
    if (len(li) == 3):
        stack.append(li)
    if (not stack): # 처음에 이 예외처리 빼먹었다
        continue
    stack[-1][2] -= 1
    if (stack[-1][2] == 0):
        score += stack.pop()[1]
print(score)


