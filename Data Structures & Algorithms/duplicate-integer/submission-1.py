class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []

        for i in nums:
            if i not in new:
                new.append(i)
            else:
                return True
        return False
        