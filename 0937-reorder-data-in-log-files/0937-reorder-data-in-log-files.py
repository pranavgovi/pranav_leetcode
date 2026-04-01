class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        from functools import cmp_to_key
        letterLogs=[]
        digitLogs=[]
        for ind,log in enumerate(logs):
            arr = log.split(" ",1)
            ide =arr[0]
            content = arr[1]
            if content[0].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append( [ide,content, ind])
        
        def compare(ar1, ar2):
            id1, id2 =  ar1[0], ar2[0]
            cont1, cont2 = ar1[1], ar2[1]
            content1, content2 =  cont1.split(), cont2.split()
            if content1==content2:
                if id1>id2:
                    return 1
                else:
                    return -1
            n1 ,n2 = len(content1), len(content2)
            i,j= 0,0
            while i<n1 and j<n2 and content1[i]==content2[j]:
                i+=1
                j+=1
            

            
            if i<n1 and j<n2:
                if content1[i]<content2[j]:
                    return -1
                else:
                    return 1
            
            if i<n1:
                return 1
            elif j<n2: #this means it is left out
                return -1
            
            


        print(letterLogs)
        letterLogs.sort(key = cmp_to_key(compare))
        #work for digitLogs is done
        #now try to write a custom sorting for letter logs

        answer=[]
        for ar in letterLogs:
            _, _, ind= ar
            answer.append(logs[ind])
        return answer+digitLogs