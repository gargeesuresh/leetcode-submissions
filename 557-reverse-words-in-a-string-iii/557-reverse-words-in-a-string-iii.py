class Solution:
    def reverseWords(self, s: str) -> str:
        lists=list(s.split(" "))
        ans=(" ").join(lists[::-1])
        return ans[::-1]