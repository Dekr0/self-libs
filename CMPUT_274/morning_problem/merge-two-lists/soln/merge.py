# Name: Chengxuan Li
# Get the input

fl = input().split()

# now do something similar to get the list of vehicles in the right lane

sl = input().split()

# Solve the problem

hw = []

for i in range(max(len(fl), len(sl))):
    if i < len(fl):
        hw.append(fl[i])
    if i < len(sl):
        hw.append(sl[i])

# Print the result
print(" ".join(hw))
