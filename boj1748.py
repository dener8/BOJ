# 1748
input = __import__('sys').stdin.readline
n = int(input())
ans = 0
li = []
for i in range(1, 9):
    li.append(9*(10**(i-1))*i)
for i in range(len(str(n))-1):
    ans += li[i]
ans += (n - (10**(len(str(n))-1)-1)) * len(str(n))
print(ans)