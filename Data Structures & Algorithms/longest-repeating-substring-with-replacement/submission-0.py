class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        counts = {}

        for r in range(len(s)):
            # Include the new character in the window.
            counts[s[r]] = counts.get(s[r], 0) + 1

            # Shrink until the window needs at most k changes.
            while (r - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            # The window is now valid.
            longest = max(longest, r - left + 1)

        return longest
        