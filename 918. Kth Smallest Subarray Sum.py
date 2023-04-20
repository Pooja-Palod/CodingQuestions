'''Given an integer array nums of length n and an integer k, return the kth smallest subarray sum.

A subarray is defined as a non-empty contiguous sequence of elements in an array. A subarray sum is the sum of all elements in the subarray.

 

Example 1:

Input: nums = [2,1,3], k = 4
Output: 3
Explanation: The subarrays of [2,1,3] are:
- [2] with sum 2
- [1] with sum 1
- [3] with sum 3
- [2,1] with sum 3
- [1,3] with sum 4
- [2,1,3] with sum 6 
Ordering the sums from smallest to largest gives 1, 2, 3, 3, 4, 6. The 4th smallest is 3.
Example 2:

Input: nums = [3,3,5,5], k = 7
Output: 10
Explanation: The subarrays of [3,3,5,5] are:
- [3] with sum 3
- [3] with sum 3
- [5] with sum 5
- [5] with sum 5
- [3,3] with sum 6
- [3,5] with sum 8
- [5,5] with sum 10
- [3,3,5], with sum 11
- [3,5,5] with sum 13
- [3,3,5,5] with sum 16
Ordering the sums from smallest to largest gives 3, 3, 5, 5, 6, 8, 10, 11, 13, 16. The 7th smallest is 10.'''

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def number_of_subarray_sum_less_than_x(x):
            cnt = cur = j = 0
            for i in range(n):
                cur += nums[i]
                while cur > x:
                    cur -= nums[j]
                    j += 1
                cnt += i - j + 1
            return cnt
        n, low, high = len(nums), min(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if k <= number_of_subarray_sum_less_than_x(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
