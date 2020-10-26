# Name: Chengxuan Li

# read the input

s = list(i for i in input())

# solve the problem

m = 0

for i in range(len(s)):
    lb = i-1
    ub = i+1
    l = 1
    while lb >= 0 and ub < len(s):
        if s[lb] == s[ub]:
            l += 2
            lb -= 1
            ub += 1
            continue
        break
    if l > m:
        m = l

print(m)