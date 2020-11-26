# Chengxuan Li
n_c = int(input())
# x, y, r
c_l = []
for i in range(n_c):
    c_l.append([float(i) for i in input().split()])
n_p = int(input())
# x, y
p_l = []
for i in range(n_p):
    p_l.append([float(i) for i in input().split()])

for p in p_l:
    flag = True
    for c in c_l:
        if abs((p[0]-c[0])) <= c[2] and abs((p[1]-c[1])) <= c[2] and (p[0]-c[0])**2+(p[1]-c[1])**2 <= c[2]**2:
                flag = False
                print("Large")
                break
    if flag:
        print("Small")