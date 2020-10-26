if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    for i in range(0, len(nums)):
        num = nums[i] if i == 0 else nums[i] * nums[i-1]
        print("%d" % num, end=" ")
    print("\n")        
