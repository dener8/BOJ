# 1463

'''
1: 0
2: 2 -> 1
3: 3 -> 1
4: 4 -> 2 -> 1
5: 5 -> 4 -> 2 -> 1
6: 6 -> 2 -> 1
7: 7 -> 6 -> 2 -> 1
8: 8 -> 4 -> 2 -> 1
9: 9 -> 3 -> 1
10: 10 -> 9 -> 3 -> 1
11: 11 -> 10 -> 9 -> 3 -> 1
12: 12 -> 4 -> 2 -> 1

dp = [0, 0, 1, 1, 2, 3, 2, 3]
      0  1  2  3  4  5  6  7
i = 8일 때, min(li[i-1], li[i//3], li[i//2])
'''

input = __import__('sys').stdin.readline
n = int(input())
dp = [0, 0, 1, 1, 2, 3, 2, 3]
val = 0
for i in range(8, 1000001):
    if i % 3 == 0 and i % 2 == 0:
        val = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif i % 3 == 0 and i % 2 != 0:
        val = min(dp[i//3], dp[i-1]) + 1
    elif i % 3 != 0 and i % 2 == 0:
        val = min(dp[i//2], dp[i-1]) + 1
    elif i % 3 != 0 and i % 2 != 0:
        val = dp[i-1] + 1
    dp.append(val)
print(dp[n])