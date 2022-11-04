# 1343
input = __import__('sys').stdin.readline
msg = list(input().rstrip())
msg.append('.')
ans = []
cnt = 0
flag = 1
for i in range(len(msg)):
    if (msg[i] == '.'):
        while True:
            if (cnt == 1):
                flag = 0
                break
            if (cnt == 0):
                break
            if (cnt - 4 >= 0):
                cnt -= 4
                ans.append("AAAA")
            elif (cnt - 2 >= 0):
                cnt -= 2
                ans.append("BB")
        ans.append('.')
    else:
        cnt += 1

    if (flag == 0):
        break

if not flag:
    print(-1)
else:
    print(''.join(ans[:-1]))

