# Given an array of ints, return True if the array is length 1 or more, and the
# first element and the last element are equal.

def same_first_last(nums):
    valid_length = len(nums) >= 1
    return valid_length and nums[0] == nums[-1]
