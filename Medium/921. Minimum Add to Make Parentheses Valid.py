class Solution(object):
    def minAddToMakeValid(self, s):
        n=len(s)
        hashmap={"(":0}
        result=0
        for i in s:
            if (i == "("):
                hashmap["("]+=1
            if(i==")"):
                if(hashmap["("]>=1):
                    hashmap["("]-=1
                else:
                    result+=1
        result=result+hashmap["("]
        return result            
            
         

        
