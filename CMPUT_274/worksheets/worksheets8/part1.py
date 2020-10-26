dic = {}
fin = open("key-value1.txt", "r")
for line in fin:
    k, v = line.strip().split("|")
    dic[k] = v
fin.close()
print(dic)
