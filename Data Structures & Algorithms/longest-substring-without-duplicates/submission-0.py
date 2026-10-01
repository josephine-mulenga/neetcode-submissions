class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        n = len(s)
        sett = set()

        for r in range(n):
            while s[r]in sett:
                sett.remove(s[left])
                left += 1
            
            w = (r-left)+ 1
            longest = max(w,longest)
            sett.add(s[r])
        return longest

            
        