# 1439
input = __import__('sys').stdin.readline
s = input().rstrip()
zeroList = s.split('1')
oneList = s.split('0')
ans = [0, 0]
for i in range(len(zeroList)):
    if zeroList[i] != '':
        ans[0] += 1
for i in range(len(oneList)):
    if oneList[i] != '':
        ans[1] += 1
print(min(ans))