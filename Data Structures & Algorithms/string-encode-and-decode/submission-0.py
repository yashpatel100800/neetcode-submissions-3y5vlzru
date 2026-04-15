class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc += str(len(i)) + ":" + i
        return enc

    def decode(self, s: str) -> List[str]:
        j = 0
        dec = []
        lengthStr = ""
        while(j<len(s)):
            while(s[j]!=":"):
                lengthStr+=s[j]
                j+=1
            length = int(lengthStr)
            dec.append(s[j+1:j+1+length])
            lengthStr = ""
            
            j = j+1+length
            
        return dec
