# Name: Chengxuan Li

# read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())


# solve the problem
area = abs(x1 - x2) * abs(y1 - y2)


# output the result
print(area)
