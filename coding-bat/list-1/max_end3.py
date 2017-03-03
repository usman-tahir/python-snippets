# Given an array of ints length 3, figure out which is larger, the first or last
# element in the array, and set all the other elements to be that value. Return
# the changed array.

def max_end3(nums):
    largest = nums[0] if nums[0] > nums[-1] else nums[-1]
    return [largest] * 3
