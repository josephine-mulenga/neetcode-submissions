class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char = []
        for i in s:
            if i.isalnum():
                char.append(i)
        
        word = "".join(char)
        reverse = ""
        while char:
            last = char.pop()
            reverse += last
            del last
        
        return word == reverse

                