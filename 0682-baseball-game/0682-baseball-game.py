class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        count=0
        for i in operations:
            if i.isdigit():
                count+=int(i)
                record.append(int(i))
                
            elif i=='C':
                count=count-(record[-1])
                record.pop(-1)
                
            elif i=='D':
                count+=(record[-1]*2)
                record.append(record[-1]*2)
                
            elif i=='+':
                count+=(record[-1]+record[-2])
                record.append(record[-1]+record[-2])
            
            elif int(i)<0:
                count+=int(i)
                record.append(int(i))
                
        
        return count
            