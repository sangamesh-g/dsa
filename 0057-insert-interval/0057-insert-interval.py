# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         i=0
#         n=len(intervals)
#         res=[]
#         while i<n and intervals[i][1]<newInterval[0]:
#             res.append(intervals[i])
#             i+=1
#         while i<n and intervals[i][0]<=newInterval[1]:
#             newInterval=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
#             i+=1
#         res.append(newInterval)
        
#         while i<n:
#             res.append(intervals[i])
#             i+=1       

#         return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        n=len(intervals)
        while i<n and intervals[i][0]<=newInterval[0]:
            i+=1
        intervals.insert(i,newInterval)
        print(intervals)
        results=[intervals[0]]
        for st,end in intervals[1:]:
            last_st,last_end=results[-1]

            if st<=last_end:
                if end>last_end:
                    results[-1][1]=end

            else:
                results.append([st,end])

        return results