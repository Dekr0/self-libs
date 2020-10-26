dic = {}
fin = open("key-value2.txt", "r")
for line in fin:
    k, v = line.strip().split("|")
    dic[k] = v.strip(" ").split(",")
fin.close()

while True:
    try:
        print(dic)
        cmd, k, v = input(">>>").split("|")
        if k in dic.keys():
            if cmd == "add":
                dic[k].append(v)
                continue
            elif cmd == "del":
                if v in dic[k]:
                    dic[k].remove(v)
                    continue
                print("No such value")
                continue
            else:
                print("No such command")
                continue
            print("No such key")
    except EOFError:
        break
    except ValueError:
        print("Invalid Input Format")
