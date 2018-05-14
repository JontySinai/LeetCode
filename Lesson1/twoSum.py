"""
Given an array of integers, return indices of the two numbers such that they add up to a 
specific target. You may assume that each input would have exactly one solution, and you 
may not use the same element twice.
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums)
    nums_set = set(nums)

    for idx in range(n):
        dif = target - nums[idx] # complement

        if dif in nums_set:
            dif_idx = nums.index(dif) # check that complement isn't self
            if idx != dif_idx:
                if idx < dif_idx:
                    return [idx, dif_idx]
                else:
                    return [dif_idx, idx]
                


nums = [3,4,3]
target = 6

ans = twoSum(nums=nums, target=target)
print(ans)




