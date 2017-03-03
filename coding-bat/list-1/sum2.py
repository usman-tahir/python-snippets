# Given an array of ints, return the sum of the first 2 elements in the array.
# If the array length is less than 2, just sum up the elements that exist,
# returning 0 if the array is length 0.

def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return sum(nums)
    return sum(nums[0:2])
