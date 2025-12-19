#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def majorityElmt(self, nums:List[int])->int:
        from collections import Counter
        freq = Counter(nums)
        max_key = max(freq, key =freq.get)
        return max_key
s = Solution()
print(s.majorityElmt([3,2,3]))