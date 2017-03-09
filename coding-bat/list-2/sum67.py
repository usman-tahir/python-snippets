# Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.

def sum67(nums):
    if not 6 in nums:
        return sum(nums)
    elif len(nums) == 0:
        return 0
    else:
        total = 0
        i = 0
        while i < len(nums):
            if nums[i] == 6:
                while nums[i] != 7:
                    i += 1
                i += 1
            if i < len(nums) and nums[i] != 6:
                total += nums[i]
                i += 1
        return total
