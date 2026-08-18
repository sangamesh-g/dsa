class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(s)!=len(pattern):
            return False

        pmap={}
        word=set()

        for i,ch in enumerate(pattern):

            if ch in pmap:
                if pmap.get(ch)!=s[i]:
                    return False

            else:
                if s[i] in word:
                    return False
                pmap[ch]=s[i]
                word.add(s[i])

        return True