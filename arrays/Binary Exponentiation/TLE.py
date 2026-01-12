class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prod=1
        for i in nums:
            prod=prod*i
        mapper={}
        for i in range(2,round(math.sqrt(prod))+1,1):
            while(prod%i==0):
                prod/=i
                if i not in mapper:
                    mapper[i]=1
                else:
                    mapper[i]+=1
        if prod>1:
            if prod not in mapper:
                mapper[prod]=1
            else:
                mapper[prod]+=1
        print(mapper)
        return len(mapper)
