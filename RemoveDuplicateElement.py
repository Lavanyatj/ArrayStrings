from typing import List
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        # st = set(nums)
        # return len(st)
        left = 0
        right = len(nums) -1
        while left <=right:
            if nums[left] == nums[right]:
                nums[left] = nums[right]
                right -=1
            else:
                left +=1
        return left
s =Solution()
print(s.removeDuplicates([1,1,2]))