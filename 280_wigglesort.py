''' 280.https://leetcode.com/problems/wiggle-sort/
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.'''


import sys, ast
from typing import List
import argparse

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(len(nums)-1):
            if ((i%2==0 )and (nums[i] > nums[i + 1])) or ((i % 2 == 1) and (nums[i] < nums[i + 1])):
            
                nums[i],nums[i+1]=nums[i+1],nums[i]
        print(nums)




parser=argparse.ArgumentParser()
parser.add_argument("--list",nargs="*",type=int)
args = parser.parse_args()
s=Solution()
print(s.wiggleSort(args.list))
print(args.list)



                
                
        
          
                