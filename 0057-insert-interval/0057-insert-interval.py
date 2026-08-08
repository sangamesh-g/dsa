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