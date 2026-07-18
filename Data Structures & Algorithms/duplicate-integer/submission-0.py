class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for num in nums:
            if num in new:
                return True
            else:
                new.add(num)
        
        return False
        