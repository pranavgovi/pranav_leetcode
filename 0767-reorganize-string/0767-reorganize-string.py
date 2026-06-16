class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        always place the higher frequent elemtns first to spreaf out
        a b a
        """
        lookup= defaultdict(int)
        for i in s:
            lookup[i]+=1
        myheap=[]
        for char, value in lookup.items():
            heapq.heappush(myheap, (-value, char))
        ans = []

        while myheap:
            val , char = heapq.heappop(myheap)
            
            if not ans or  ans[-1]!= char:
                #directly add the char
                ans.append(char)
                val+=1
                if val!=0:
                    heapq.heappush(myheap, (val, char))
            else:
                if not myheap:
                    return ''
                else:
                    val1, char1 =  heapq.heappop(myheap)
                    ans.append(char1)
                    val1+=1
                    if val1!=0:
                        heapq.heappush(myheap, (val1, char1))
                    heapq.heappush(myheap, (val, char))
        return ''.join(ans)



