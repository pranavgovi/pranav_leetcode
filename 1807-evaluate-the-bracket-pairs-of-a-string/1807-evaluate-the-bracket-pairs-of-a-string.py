class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = {}
        for i in knowledge:
            key,value = i
            lookup[key]=value
    
        ans=[]
        j=0
        n=len(s)
        prev_str=[]
        while j<n:

            if s[j]=='(':
                #check if there is a prev str stored
                if prev_str:
                    ans.append(''.join(prev_str))
                    prev_str=[]
                start=j
                #start extracting the key
                while s[j]!=')':
                    j+=1
                key = s[start+1:j]
                if key not in lookup:
                    ans.append('?')
                else:
                    ans.append(lookup[key])
                j+=1
            else:
                prev_str.append(s[j])
                j+=1
        
        if prev_str:
            ans.append(''.join(prev_str))

        return ''.join(ans)