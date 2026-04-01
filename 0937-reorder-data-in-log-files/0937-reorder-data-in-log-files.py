class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        from functools import cmp_to_key
        letterLogs=[]
        digitLogs=[]
        for ind,log in enumerate(logs):
            arr = log.split(" ",1)
            ide =arr[0]
            content = arr[1]
            content =content.split()
            if content[0].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append([[ide]+content,ind])
        
        def compare(ar1, ar2):
            arr1= ar1[0]
            arr2= ar2[0]
            content1 = arr1[1:]
            content2= arr2[1:]
            if content1==content2:
                if arr1[0]>arr2[0]:
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
            _, ind= ar
            answer.append(logs[ind])
        return answer+digitLogs