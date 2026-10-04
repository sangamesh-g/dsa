class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_q=deque()
        min_q=deque()
        ans=0
        left=0
        n=len(nums)

        for right in range(n):

            while max_q and nums[max_q[-1]]<=nums[right]:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]]>=nums[right]:
                min_q.pop()
            min_q.append(right)

            while nums[max_q[0]]-nums[min_q[0]]>limit:
                if max_q[0]==left:
                    max_q.popleft()
                
                if min_q[0]==left:
                    min_q.popleft()
                
                left+=1
            
            ans=max(ans,right-left+1)

        return ans