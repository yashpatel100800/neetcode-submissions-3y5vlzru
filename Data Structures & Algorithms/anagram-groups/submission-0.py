class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for st in strs:
            temp = [0]*26
            for i in st:
                temp[ord(i)-ord("a")]+=1
            arr[tuple(temp)].append(st) 
        
        return list(arr.values())