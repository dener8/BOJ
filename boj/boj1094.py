# 1094
input = __import__('sys').stdin.readline
x = int(input())
li = []
while x != 0: # 결국 이진수 변환 문제!
    li.append(x % 2)
    x //= 2
print(sum(li))

