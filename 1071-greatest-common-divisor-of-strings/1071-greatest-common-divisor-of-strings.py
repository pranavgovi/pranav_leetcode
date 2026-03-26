class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #to have a common splitter, they should follow the conditio str1+str2 == str2+str1
        if str1+str2!= str2+str1:
            return ""
        #find gcd
        n1, n2= len(str1), len(str2)

        a ,b = max(n1, n2), min(n1, n2)

        while b:

            a, b = b , a%b
        return str1[:a]