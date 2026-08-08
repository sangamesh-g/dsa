class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        results=[intervals[0]]
        for st,end in intervals[1:]:
            lt_st,lt_end=results[-1]
            if st<=lt_end:
                if end>lt_end:
                    results[-1][1]=end
            else:
                results.append([st,end])

        return results