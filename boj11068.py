# 11068
input = __import__('sys').stdin.readline
n = int(input())
for _ in range(n):
    num = int(input())
    for i in range(2, 65):
        s = num
        li = []
        while s:
            li.append(s % i)
            s = s // i
        flag = 1
        for j in range(len(li) // 2):
            if li[j] != li[len(li)-1-j]:
                flag = 0
                break
        if flag == 1:
            break
    print(flag)




