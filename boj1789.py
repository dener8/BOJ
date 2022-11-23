# 1789
input = __import__('sys').stdin.readline
s = int(input())
sum = 0
i = 0
while True:
    if s < sum:
        ans = i-1
        break
    i += 1
    sum += i
print(ans)

'''
1 1 # 1
2 1
3 2 # 1+2
4 2
5 2
6 3 # 1+2+3
7 3
8 3
9 3
10 4 # 1+2+3+4
11 4
blah blah
'''

