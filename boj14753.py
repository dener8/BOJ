# 14753
input = __import__('sys').stdin.readline
n = int(input())
li = list(map(int,input().split()))
li.sort()
ans = [li[0]*li[1], li[0]*li[1]*li[2], li[-1]*li[-2], li[-1]*li[-2]*li[-3],
       li[0]*li[-1], li[0]*li[1]*li[-1], li[0]*li[-2]*li[-1]]
print(max(ans))