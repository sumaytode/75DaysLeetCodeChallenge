class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for i in strs:
            key="".join(sorted(i))
            if key not in hash:
                hash[key]=[]
            hash[key].append(i)
        return list(hash.values())