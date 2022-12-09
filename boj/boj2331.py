# 2331
input = __import__('sys').stdin.readline
a, p = map(int, input().split())
li = [a]
while True:
    n = str(li[-1])
    sm = 0
    for i in range(len(n)):
        sm += (int(n[i])) ** p
    if sm in li:
        break
    li.append(sm)
for i in range(len(li)):
    if li[i] == sm:
        print(i)

''' 
중복이 나오면 멈추고, 그 인덱스를 찾아라 => 인덱스 자체를 출력하면 그게 답이 됨
'''