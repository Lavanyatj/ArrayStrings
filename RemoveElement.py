#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val:int) -> int:
        left =0
        right = len(nums)-1
        while left <= right:
            if nums[left] == val:
                nums[left] =nums[right]
                right -=1
            else:
                left +=1
        return left
s = Solution()
print(s.removeElement([3,2,2,3],3))