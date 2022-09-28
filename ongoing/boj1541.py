# 1541
# 괄호가 없는 식에 괄호를 쳐서 식의 결과가 최소가 되게 만들기
#
input = __import__('sys').stdin.readline
s = input().rstrip()
li = []
start = 0
for i in range(len(s)):
    if s[i] == '+' or s[i] == '-':
        li.append(int(s[start:i]))
        start = i
    if i == len(s)-1:
        li.append(int(s[start:]))



