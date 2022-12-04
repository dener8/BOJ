# 3036
input = __import__('sys').stdin.readline
n = int(input())
li = list(map(int,input().split()))
for i in range(1, n):
     a = li[0]
     b = li[i]
     if b == 1:
         print('{}/{}'.format(a, b))
         continue
     val = 2
     while val <= b:
         if a%val==0 and b%val==0:
             a //= val
             b //= val
             val = 2
             continue
         val += 1
     print('{}/{}'.format(a, b))

# math의 gcd를 이용할 수도 있다!