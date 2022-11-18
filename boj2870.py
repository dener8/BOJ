# 2870
input = __import__('sys').stdin.readline
n = int(input())
ans = []
for _ in range(n):
    s = input().rstrip()
    temp = ''
    start = 0
    for i in range(len(s)):
        if (ord('0') <= ord(s[i]) <= ord('9')):
            temp += s[i]
        else:
            if (temp != ''):
                ans.append(int(temp))
            temp = ''
    if (temp != ''):
        ans.append(int(temp))
ans.sort()
for i in range(len(ans)):
    print(ans[i])


