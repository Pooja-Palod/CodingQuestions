'''


Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.'''


 class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        ans,r=0,0
        zero=0
        while r<n:
            if nums[r]==0:
                zero+=1
            while zero>1:
                if nums[l]==0:
                    zero-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
