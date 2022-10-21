# 11637
input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    for i in range(n):
        li.append(int(input()))
    sl = sorted(li)
    if sl[-1] == sl[-2]: # 최고 득표가 두 명이라 winner가 없는 경우
        print("no winner")
    else:
        if sum(sl[:-1]) < sl[-1]:
            sign = "majority winner"
        else:
            sign = "minority winner"
        for j in range(n):
            if li[j] == sl[-1]:
                idx = j + 1
                break
        print(sign, idx)




