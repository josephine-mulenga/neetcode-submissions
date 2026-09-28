class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ""
        for word in strs:
            new += f"{len(word)}" + "#" + word
        return new

        

    def decode(self, s: str) -> List[str]:
        og = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            og.append(s[start:start + length])
            i = start + length

        return og

