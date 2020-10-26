# Name: Chengxuan Li
#Good Luck! You've got this! :)
k, m = [int(i) for i in input().split()]

r = m
c = []

while True:
    if r - k > 0:
        r -= k
        c.append(k)
        k -= 1
        continue
    c.append(r)
    break

"""
while m > 0:
    if n <= m:
        c.append(n)
    elif n > m:
        c.append(m)
        m = 0
    n -= 1
    
print(len(c))
print(*a[::-1]) #[s:e:st] with s = start (inclusive), e = end (exclusive), st = step
"""

c.reverse()
print(len(c))
print(*c)