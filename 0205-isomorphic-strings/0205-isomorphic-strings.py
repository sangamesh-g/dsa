class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        map={}
        x=set()
        y=set()
        for i,ch in enumerate(s):
            if ch in map:
                if t[i]!=map.get(ch):
                    print('t[i]!=map.get(ch)')
                    return False
            else:
                if ch in x or t[i] in y:
                    print('ch in x')
                    return False
                map[ch]=t[i]
                x.add(ch)
                y.add(t[i])
        
        return True