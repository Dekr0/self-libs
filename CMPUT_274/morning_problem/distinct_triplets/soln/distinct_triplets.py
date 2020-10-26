# Read input here.
n = int(input().strip())

# Solve problem here. Good luck!

count = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        count += ((n-1)-j)

print(count)
