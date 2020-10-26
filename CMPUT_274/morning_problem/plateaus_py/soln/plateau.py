# Name: Chengxuan Li
# Good luck! Write your solution below.

nums = list(map(int, input().split()))

abs_max = 0
now_max = 0
prev_num = None

for i in nums:
    if i == prev_num:
        now_max += 0
        abs_max = max((abs_max, now_max))
    else:
        prev_num = i
        now_max = 0

print(abs_max)
