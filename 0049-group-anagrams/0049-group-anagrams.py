class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansdict=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            ansdict[key].append(s)

        return list(ansdict.values())