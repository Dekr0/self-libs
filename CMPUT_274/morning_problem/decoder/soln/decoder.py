# Read in the input
total = int(input())
dic = {}
coded_text = None
while True:
    line = input().split()
    if len(line) < 2:
        coded_text = line[0]
        break
    dic[line[0]] = line[1]

# Solve the problem, good luck!

words = []
tmp_word = ""

for i in coded_text:
    tmp_word = tmp_word + i
    if tmp_word in dic.keys():
        words.append(dic[tmp_word])
        tmp_word = ""

print(*words)