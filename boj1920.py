# 1920
# 시간복잡도: 100,000 * 100,000 => 브루트포스 불가능
input = __import__('sys').stdin.readline
n = int(input())
n_li = list(map(int,input().split()))
n_li.sort()
m = int(input())
m_li = list(map(int,input().split()))
for i in m_li:
    left = 0
    right = n-1
    while True:
        if left > right:
            print(0)
            break
        mid = (left+right) // 2     # 괄호 좀 빼먹지 말아라
        if n_li[mid] > i:
            right = mid - 1
        elif n_li[mid] < i:
            left = mid + 1
        else:
            print(1)
            break


