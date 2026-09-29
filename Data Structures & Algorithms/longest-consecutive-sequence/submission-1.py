class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                current = num
                count = 1
            
                while current + 1 in nums:
                        count += 1
                        current = current + 1

                longest = max(count, longest)
            
        
        return longest
