class Solution:
    def reverseWords(self, s: str) -> str:
        """
        split automatically removes leading and trailing spaces
        """
        l = s.split()
        l.reverse()
        return " ".join(l)
    

