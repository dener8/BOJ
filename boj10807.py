# 10807
n = int(input())
li = list(map(int,input().split()))
v = int(input())
cnt = 0
for i in range(len(li)):
    if li[i] == v:
        cnt +=1
print(cnt)