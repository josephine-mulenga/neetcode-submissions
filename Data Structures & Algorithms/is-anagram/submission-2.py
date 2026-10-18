'''
Understand:
Input: two string s and t
output: Boolean(True if two string are anagrams and False if not)
Edge cases: 
- if one string is empty return false
- if len(s) != len(t) return False



Plan
- convert s to a list and t to a list as well
- sort s list
- sort t list
- if s == t: return true, Else return false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        
        if len(s) != len(t):
            return False

        S = list(s)
        T = list(t)
        S.sort()
        T.sort()

        if S != T:
            return False
        return True