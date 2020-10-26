# Read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# Solve the problem
xs = (x1, x2, x3)
ys = (y1, y2, y3)

width = max(xs) - min(xs)
height = max(ys) - min(ys)

if xs.count(max(xs)) > xs.count(min(xs)):
    corner_x = max(xs) - width
else:
    corner_x = min(xs) + width

if ys.count(max(ys)) > ys.count(min(ys)):
    corner_y = max(ys) - height
else:
    corner_y = min(ys) + height
# Output the result

print("%d %d" % (corner_x, corner_y))
