# Name: Chengxuan Li

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = sorted(x)
y = sorted(y)

sum = 0
for i in range(n):
    sum += x[i]*y[i]

print(sum)