class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)
        n = len(s1)
        for i in range(0,len(s2)):
            s2Counter = Counter(s2[i:i+n])
            if(s1Counter == s2Counter):
                return True
        return False
        