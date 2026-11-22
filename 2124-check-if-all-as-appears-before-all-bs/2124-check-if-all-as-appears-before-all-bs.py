class Solution:
    def checkString(self, s: str) -> bool:
        a_flag = False
        b_flag=False
        #if a comes after b , surely return
        for i in s:
            if i=="a":
                if b_flag:
                    return False
                a_flag= True
            else:
                #there can be a case where its all a's
                b_flag=True
                

        return True