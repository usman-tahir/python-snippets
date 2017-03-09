# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.

def sum13(nums):
    for e in range(len(nums)):
        if nums[e] == 13 and e != len(nums) - 1:
            nums[e] = 0
            nums[e + 1] = 0
        elif nums[e] == 13:
            nums[e] = 0
    return sum(nums)
