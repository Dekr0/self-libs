with open("unsort_list.txt", "r") as fin:
    ul = fin.read().split()
    ul.sort()
