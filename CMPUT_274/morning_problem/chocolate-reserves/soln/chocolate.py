# Name: Chengxuan Li


line = input().split()
chocolates = int(line[0])
jars = int(line[1])
count = 0

# write your code here

for i in range(jars):
    stored, max_cap = list(map(int, input().split()))
    if stored + chocolates <= max_cap:
        count += 1

print(count)
