from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result=[]
        for i in strs:
            result=[]
            for j in strs:
                if sorted(i) == sorted(j):
                    result.append(j)
            if result not in final_result:
                final_result.append(result)

        return final_result

obj = Solution()
print(obj.isAnagram("anagram", "nagaram")) #True
print(obj.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))