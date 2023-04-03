'''There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.
Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1. 
'''

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        #jump line
        #For a day i, try painting all areas in the range. If the area is empty, set the value on the number line to end_i, and increment the amount painted on that day.If the area has been painted previously, jump to the end of the painted range (which was recorded on the number line on a previous day).
        line, res = [0] * 50001, [0] * len(paint)
        for i,(start,end) in enumerate(paint):
            while start<end:
                jump=max(line[start],start+1)
                res[i] += 1 if line[start] == 0 else 0
                line[start]=max(line[start],end)
                start=jump
        return res
