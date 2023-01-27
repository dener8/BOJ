# 17300
input = __import__('sys').stdin.readline
n = int(input())
li = list(map(int, input().split()))
oppositeList = [[1, 3], [4, 6], [7, 9], [1, 7], [2, 8], [3, 9], [1, 9], [3, 7]]
pattern = [0] * 10
ans = "YES"
pattern[li[0]] += 1
for i in range(1, len(li)):
    for pair in oppositeList:
        if sorted([li[i-1], li[i]]) == pair and pattern[(li[i-1] + li[i]) // 2] == 0:
            print("NO")
            exit()
    pattern[li[i]] += 1

for i in pattern:
    if i > 1:
        print("NO")
        exit()
print(ans)