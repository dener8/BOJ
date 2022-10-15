# 2659
input = __import__('sys').stdin.readline
num = list(input().split())
mn = 10000
for i in range(4):
    temp = int(''.join(num[i:] + num[:i]))
    mn = min(mn, temp)
res = mn

#시계수 리스트 만들기
time_li = []
for k in range(1111, 10000):
    mn = 10000
    for i in range(4):
        mn = min(mn, int(str(k)[i:] + str(k)[:i]))
    if '0' not in str(k) and mn not in time_li:
        time_li.append(mn)
for i in range(len(time_li)):
    if time_li[i] == res:
        print(i+1)
        break

# 이렇게 더럽게 풀 문제가 아닌 것 같은데 ㅡㅡ