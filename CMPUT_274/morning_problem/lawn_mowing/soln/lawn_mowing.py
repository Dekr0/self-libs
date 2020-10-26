# Name: Chengxuan Li
# Good luck! You've got this!

[l, w] = list(map(int, input().split()))
total = min([l,w])
if l == w:
    for i in range(4):
        total += l**2*(i+1)
else:
    for i in range(2):
        total += 2*max([l,w])*min([l,w])*(i+1)
print(int(total))