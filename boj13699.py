# 13699
input = __import__("sys").stdin.readline
n = int(input())
li = [1, 1, 2]
for _ in range(33):
    val = 0
    for j in range(len(li)):
        val += li[j] * li[-1-j]
    li.append(val)
print(li[n])