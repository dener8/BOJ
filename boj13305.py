# 13305
input = __import__('sys').stdin.readline
# 1km당 1리터 사용
# 기름 값을 계속 밀고 나가면서, 기름 값이 싸질 때 값의 변화를 주는 방식으로 하면 될 듯
# => 그리디!
n = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))
val = price[0]
ans = 0
for i in range(len(price)-1):
    if price[i] < val:
        val = price[i]
    ans += val * dist[i]
print(ans)
