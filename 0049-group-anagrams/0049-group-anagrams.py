class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp=[]
        for s in strs:
            temp.append("".join(sorted(s)))

        ansdict=defaultdict(list)
        for i in range(len(strs)):
            ansdict[temp[i]].append(strs[i])
        print(ansdict)
        
        return list(ansdict.values())