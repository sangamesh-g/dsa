class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        preSumMap = {0:1}
        result = 0

        for num in nums:
            currentSum += num 
            
            requiredSum = currentSum - k
            if requiredSum in preSumMap:
                result += preSumMap[requiredSum]
            
            if currentSum in preSumMap:
                preSumMap[currentSum] += 1
            else:
                preSumMap[currentSum] = 1
            
        return result