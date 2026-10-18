'''
Understand:
Input: List of intergers
Output: Boolean (true if any value appears more than once and false otherwise)
Edge cases: Empty list

Plan
- create dictionary to store value and the number of times it appears
- iterate over dictionary to see if any keys have a value greater than 1
return true if any value is greater than 1 else, false
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        values = {}
        for i in nums:
            values[i] = values.get(i,0) +1
        
        for value in values.values():
            if value >= 2:
                return True
        
        return False
