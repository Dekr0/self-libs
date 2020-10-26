# Distinct Triples Morning Problem
# n = 673
n = int(input())
k = 3                       # Not used.  Implied.
count = 0
for i in range(n):
    for j in range(i+1, n):  # Minor flaw here
        count += (n - j  - 1)
print(count)
