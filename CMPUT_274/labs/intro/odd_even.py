if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    for i in range(0, len(nums)):
        if not nums[i] % 2 == 0:
            print(nums[i])
        nums[i] = int(str(nums[i]) * 2)
    print(nums)
