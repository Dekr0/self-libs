# Name: Chengxuan Li

# Read in the input

scores = set(map(int, input().split()))

# Solve the problem and output the result

if not len(scores) == 3:
    result = "same" if len(scores) == 1 else "similar"
else:
    result = "distinct"

print(result)

