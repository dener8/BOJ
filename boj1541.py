# 1541
# 괄호가 없는 식에 괄호를 쳐서 식의 결과가 최소가 되게 만들기
# 1. - 를 기준으로 쪼개서 리스트에 저장한다. => 2차원 리스트
# 2. +로만 묶인 내부의 리스트들을 돌면서, + 연산을 끝낸 결과값으로 만든다.
# 3. 첫번 째 값에서 그 뒤의 값을 계속 빼주면 됨!
input = __import__('sys').stdin.readline
s = list(input().rstrip().split('-'))
li = []
for i in range(len(s)):
    temp = list(s[i].split('+'))
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    li.append(sum(temp))
ans = li[0]
for i in range(1, len(li)):
    ans -= li[i]
print(ans)