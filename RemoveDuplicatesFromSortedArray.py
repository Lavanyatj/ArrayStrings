#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1859464731/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def removeDuplicatesSA(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[j] == nums[i]:
                i +=1
                nums[i]=nums[j]
        return i+1
s = Solution()
print(s.removeDuplicatesSA([1,1,2]))