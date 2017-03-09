# Given an array of ints, return True if the array contains a 2 next to a 2
# somewhere.

def has22(nums):
    return [2, 2] in [nums[i:i + 2] for i in range(len(nums) - 1)]
