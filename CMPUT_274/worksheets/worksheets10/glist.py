from random import random

n = int(input())
fout = open("unsort_list.txt", "w")

for i in range(n):
    fout.write("%s " % random())

fout.close()

