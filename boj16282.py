# 1번 끊으면 -> 3개
# 2번 끊으면 -> 5개
# 3번 끊으면 -> 7개
input=__import__('sys').stdin.readline
n=int(input())
start=2
val=0
li=[1]
while True:
    if val > 10**18:
        break
    temp = start
    val = start
    for i in range(start-1):
        temp = temp * 2
        val += temp
    li.append(val+start-1)
    start += 1
# print(li)
for i in range(len(li)-1):
    if li[i] <= n <= li[i+1]:
        print(i+1)
        break