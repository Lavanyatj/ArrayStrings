#https://leetcode.com/problems/merge-sorted-array/submissions/1859052307/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def mergeSortedArray(self, nums1: List[int], m:int, nums2:List[int], n:int)-> List[int]:
        x = m-1
        y = n-1
        for z in range(m+n-1, -1, -1):
            if x < 0:
                nums1[z] = nums2[y]
                y -=1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -=1
            else:
                nums1[z] = nums2[y]
                y -=1
        return nums1
s = Solution()
print(s.mergeSortedArray([1,2,3,0,0,0],3,[2,5,6],3))